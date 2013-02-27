# Reversi

import random
import sys

class Reversi:
  def __init__(self, BOARD_SIZE):
    self.BOARD_SIZE = BOARD_SIZE
  
  def drawBoard(self, board): # prints out board that is passed. Returns None
    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'
  
    print '    1   2   3   4   5   6   7   8'
    print HLINE
    for y in range(self.BOARD_SIZE):
      print VLINE
      print y+1,
      for x in range(self.BOARD_SIZE):
        print '| {0}'.format(board[x][y]),
      print '|'
      print VLINE
      print HLINE


  def resetBoard(self, board): # blanks out board it is passed, except for start positions
    for x in range(self.BOARD_SIZE):
      for y in range(self.BOARD_SIZE):
        board[x][y] = ' '
  
    # Starting positions:
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

  def getNewBoard(self): # creates brand new, blank board data structure
    board = []
    for i in range(self.BOARD_SIZE):
      board.append([' '] * self.BOARD_SIZE)
    return board
  
  def isValidMove(self, board, tile, xstart, ystart):
    # Returns False if player's move is on space xstart, ystart is invalid
    # If is a valid move, returns list of spaces that would become player's
    # if they made a move there
    if board[xstart][ystart] != ' ' or not self.isOnBoard(xstart, ystart):
      return False
  
    if tile == 'X':
      otherTile = 'O'
    else:
      otherTile = 'X'
  
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
      x, y = xstart, ystart
      x += xdirection  # first step in direction
      y += ydirection
      foundOtherTiles = False
      while self.isOnBoard(x, y) and board[x][y] == otherTile:
        # there is a piece belonging to the other player next to our piece
        x += xdirection
        y += ydirection
        foundOtherTiles = True
      if not self.isOnBoard(x, y):
        # break out of while loop, then continue in for loop
        continue
      elif foundOtherTiles and board[x][y] == tile:
        # If there are othertiles next to our move
        return True
    return False
    
  def isOnBoard(self, x, y):
    # returns True if coordinated located on Board
    return 0 <= x and x < self.BOARD_SIZE and 0 <= y and y < self.BOARD_SIZE
  
  def getBoardWithValidMoves(self, board, tile): 
    # returns board with . marking valid moves a player can make
    dupeBoard = self.getBoardCopy(board)
    for x, y in self.getValidMoves(dupeBoard, tile):
      dupeBoard[x][y] = '.'
    return dupeBoard
  
  def getValidMoves(self, board, tile):
    # returns list of [x, y] lists of valid moves for given player on given board
    validMoves = []
    for x in range(self.BOARD_SIZE):
      for y in range(self.BOARD_SIZE):
        if self.isValidMove(board, tile, x, y):
          validMoves.append([x, y])
    return validMoves
  
  def getScoreOfBoard(self, board):
    # Determine the score by counting tiles. Return dictionary with keys 'X' and 'Y'
    xscore = 0
    oscore = 0
    for x in range(8):
      for y in range(8):
        if board[x][y] == 'X':
          xscore += 1
        if board[x][y] == 'O':
          oscore += 1
    return {'X': xscore, 'O': oscore}
  
  def enterPlayerTile(self):
    # let's player type in which tile they want to be
    # returns a list with player's tile as first item and computer's as second
    tile = ''
    while not(tile == 'X' or tile == 'O'):
      print 'Do you want to be X or O?'
      tile = raw_input().upper()
    
    # the first element in the tuple is player's tile, the second is computer's tile
    if tile == 'X':
      return ['X', 'O']
    else:
      return ['O', 'X']
    
  def whoGoesFirst(self):
    # randomly choose the player that goes first
    if random.randint(0, 1) == 0:
      return 'computer'
    else:
      return 'player'
    
  def playAgain(self):
    print 'Do you want to play again? (yes or no)'
    return raw_input().lower().startswith('y')
    
  def makeMove(self, board, tile, xstart, ystart):
    if not self.isOnBoard(xstart, ystart):
      return
    else:
      board[xstart][ystart] = tile

    if tile == 'X':
      otherTile = 'O'
    else:
      otherTile = 'X'
  
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
      x, y = xstart, ystart
      x += xdirection  # first step in direction
      y += ydirection
      foundOtherTiles = []
      while self.isOnBoard(x, y) and board[x][y] == otherTile:
        # there is a piece belonging to the other player next to our piece
        foundOtherTiles.append([x, y])
        x += xdirection
        y += ydirection
      if not self.isOnBoard(x, y):
        # break out of while loop, then continue in for loop
        continue
      elif board[x][y] == tile:
        # We may have found other tiles to flip
        for fx, fy in foundOtherTiles:
          #print 'Recursive move:', [fx, fy]
          self.makeMove(board, tile, fx, fy)

    # Recursive scrape
    for cx in range(self.BOARD_SIZE):
      for cy in range(self.BOARD_SIZE):
        if board[cx][cy] == tile:
          for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
            x, y = cx, cy
            x += xdirection  # first step in direction
            y += ydirection
            foundOtherTiles = []
            while self.isOnBoard(x, y) and board[x][y] == otherTile:
              # there is a piece belonging to the other player next to our piece
              foundOtherTiles.append([x, y])
              x += xdirection
              y += ydirection
            if not self.isOnBoard(x, y):
              # break out of while loop, then continue in for loop
              continue
            elif board[x][y] == tile:
              # We may have found other tiles to flip
              for fx, fy in foundOtherTiles:
                #print 'Recursive scrape move:', [fx, fy]
                self.makeMove(board, tile, fx, fy)
  
  def getBoardCopy(self, board): # duplicate board list and return duplicate
    dupeBoard = self.getNewBoard()
    for x in range(8):
      for y in range(8):
        dupeBoard[x][y] = board[x][y]
    return dupeBoard
  
  def isOnCorner(self, x, y):
    # returns True if position is in one of four corners
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)
  
  def getPlayerMove(self, board, playerTile):
    # let the player type in their move
    # returns move as [x, y] or returns string 'hints' or 'quit'
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    x = y = -1
    while True:
      print 'Enter your move, or type quit to end the game, or hints to turn off/on hints.'
      move = raw_input().lower()
      if move == 'quit':
        return 'quit'
      elif move == 'hints':
        return 'hints'
      elif len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
        x = int(move[0]) - 1
        y = int(move[1]) - 1
        if not self.isValidMove(board, playerTile, x, y):
          print 'Invalid move'
          continue
        else:
          break
      else:
        print 'That is not a valid move. Type the x digit (1-8), then the y digit (1-8).'
        print 'For example, 81 will be the top-right corner'
    print 'Valid move'
    return [x, y]

  def getComputerMove(self, board, computerTile):
    # gien a board and computer's tile, determine where to 
    # move and return that move as a [x, y] list
    possibleMoves = self.getValidMoves(board, computerTile)
    # randomize the order of the possible moves
    random.shuffle(possibleMoves)
    # always go for the corner if available
    for x, y in possibleMoves:
      if self.isOnCorner(x, y):
        return [x, y]
    # go through all possible moves and remember best scoring move
    bestScore = -1
    for x, y in possibleMoves:
      dupeBoard = self.getBoardCopy(board)
      self.makeMove(dupeBoard, computerTile, x, y)
      score = self.getScoreOfBoard(dupeBoard) [computerTile]
      if score > bestScore:
        bestMove = [x, y]
        bestScore = score
    return bestMove
  
  def showPoints(self, mainBoard, playerTile, computerTile):
    # print out current score
    scores = self.getScoreOfBoard(mainBoard)
    print 'You have {0} points. The computer has {1} points.'.format(scores[playerTile], scores[computerTile])
  
  def play(self):
    while True:
      # reset the board and game
      mainBoard = self.getNewBoard()
      self.resetBoard(mainBoard)
      playerTile, computerTile = self.enterPlayerTile()
      print 'Player tile', playerTile
      print 'Computer tile', computerTile
      showHints = False
      turn = self.whoGoesFirst()
      print 'The ' + turn + ' will go first.'
  
      while True:
        if turn == 'player':
          print 'Player turn.'
          # Player's turn:
          if showHints:
            self.drawBoard(self.getBoardWithValidMoves(mainBoard, playerTile))
          else:
            self.drawBoard(mainBoard)
          self.showPoints(mainBoard, playerTile, computerTile)
          move = self.getComputerMove(mainBoard, playerTile)
          print 'Player move', move
          if move == 'quit':
            print 'Thanks for playing!'
            sys.exit(0)
          elif move == 'hints':
            showHints = not showHints
            print 'Showing hints:', showHints
            continue
          else:
            print 'Making move:', move
            self.makeMove(mainBoard, playerTile, move[0], move[1])
          if self.getValidMoves(mainBoard, computerTile) == []:
            print 'No valid computer moves.  Ending game.'
            break
          else:
            print 'Now computer turn.'
            turn = 'computer'
        else:
          print 'Computer turn.'
          # Computer's turn:
          self.drawBoard(mainBoard)
          self.showPoints(mainBoard, playerTile, computerTile)
          raw_input("Press enter to see the computer's move.")
          x, y = self.getComputerMove(mainBoard, computerTile)
          print 'Computer move:', [x + 1, y + 1]
          self.makeMove(mainBoard, computerTile, x, y)
      
          if self.getValidMoves(mainBoard, playerTile) == []:
            print 'No valid player moves.  Ending game.'
            break
          else:
            print 'Now player turn.'
            turn = 'player'
    
      # Display the final score
      self.drawBoard(mainBoard)
      scores = self.getScoreOfBoard(mainBoard)
      print 'X scored {0} points. O score {1} points'.format(scores['X'], scores['O'])
      if scores[playerTile] > scores[computerTile]:
        print 'You beat the computer by {0} points! Gratz!'.format(scores[playerTile] - scores[computerTile])
      elif scores[playerTile] < scores[computerTile]:
        print 'You lost. The computer beat you by {0} points'.format(scores[computerTile] - scores[playerTile])
      else:
        print 'The game was a tie!'
    
      if not self.playAgain():
        break    

if __name__ == '__main__':
  print 'Welcome to Reversi!'
  while True:
    Reversi(8).play()
