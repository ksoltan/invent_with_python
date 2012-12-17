# Reversi

import random
import sys

BOARD_SIZE = 8

def drawBoard(board): # prints out board that is passed. Returns None
  HLINE = '  +---+---+---+---+---+---+---+---+'
  VLINE = '  |   |   |   |   |   |   |   |   |'
  
  print '    1   2   3   4   5   6   7   8'
  print HLINE
  for y in range(8):
    print VLINE
    print y+1,
    for x in range(8):
      print '| {0}'.format(board[x][y]),
    print '|'
    print VLINE
    print HLINE


def resetBoard(board): # blanks out board it is passed, except for start positions
  for x in range(BOARD_SIZE):
    for y in range(BOARD_SIZE):
      board[x][y] = ' '
  
  # Starting positions:
  board[3][3] = 'X'
  board[3][4] = 'O'
  board[4][3] = 'O'
  board[4][4] = 'X'

def getNewBoard(): # creates brabd new, blank board data structure
  board = []
  for i in range(BOARD_SIZE):
    board.append([' '] * BOARD_SIZE)
  return board

def isValidMove(board, tile, xstart, ystart):
  # Returns False if player's move is on space xstart, ystart is invalid
  # If is a valid move, returns list of spaces that would become player's
  # if they made a move there
  if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
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
    while isOnBoard(x, y) and board[x][y] == otherTile:
      # there is a piece belonging to the other player next to our piece
      x += xdirection
      y += ydirection
      foundOtherTiles = True
    if not isOnBoard(x, y):
      # break out of while loop, then continue in for loop
      continue
    elif foundOtherTiles and board[x][y] == tile:
      # If there are othertiles next to our move
      return True
  return False
    
def isOnBoard(x, y):
  # returns True if coordinated located on Board
  return 0 <= x and x < BOARD_SIZE and 0 <= y and y < BOARD_SIZE
  
def getBoardWithValidMoves(board, tile): 
  # returns board with . marking valid moves a player can make
  dupeBoard = getBoardCopy(board)
  for x, y in getValidMoves(dupeBoard, tile):
    dupeBoard[x][y] = '.'
  return dupeBoard
  
def getValidMoves(board, tile):
  # returns list of [x, y] lists of valid moves for given player on given board
  validMoves = []
  for x in range(8):
    for y in range(8):
      if isValidMove(board, tile, x, y):
        validMoves.append([x, y])
  return validMoves
  
def getScoreOfBoard(board):
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
  
def enterPlayerTile():
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
    
def whoGoesFirst():
  # randomly choose the player that goes first
  if random.randint(0, 1) == 0:
    return 'computer'
  else:
    return 'player'
    
def playAgain():
  print 'Do you want to play again? (yes or no)'
  return raw_input().lower().startswith('y')
    
def makeMove(board, tile, xstart, ystart):
  if not isOnBoard(xstart, ystart):
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
    while isOnBoard(x, y) and board[x][y] == otherTile:
      # there is a piece belonging to the other player next to our piece
      foundOtherTiles.append([x, y])
      x += xdirection
      y += ydirection
    if not isOnBoard(x, y):
      # break out of while loop, then continue in for loop
      continue
    elif board[x][y] == tile:
      # We may have found other tiles to flip
      for fx, fy in foundOtherTiles:
        #print 'Recursive move:', [fx, fy]
        makeMove(board, tile, fx, fy)

  # Recursive scrape
  for cx in range(BOARD_SIZE):
    for cy in range(BOARD_SIZE):
      if board[cx][cy] == tile:
        for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
          x, y = cx, cy
          x += xdirection  # first step in direction
          y += ydirection
          foundOtherTiles = []
          while isOnBoard(x, y) and board[x][y] == otherTile:
            # there is a piece belonging to the other player next to our piece
            foundOtherTiles.append([x, y])
            x += xdirection
            y += ydirection
          if not isOnBoard(x, y):
            # break out of while loop, then continue in for loop
            continue
          elif board[x][y] == tile:
            # We may have found other tiles to flip
            for fx, fy in foundOtherTiles:
              #print 'Recursive scrape move:', [fx, fy]
              makeMove(board, tile, fx, fy)
  
def getBoardCopy(board): # duplicate board list and return duplicate
  dupeBoard = getNewBoard()
  for x in range(8):
    for y in range(8):
      dupeBoard[x][y] = board[x][y]
  return dupeBoard
  
def isOnCorner(x, y):
  # returns True if position is in one of four corners
  return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)
  
def getPlayerMove(board, playerTile):
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
      if not isValidMove(board, playerTile, x, y):
        print 'Invalid move'
        continue
      else:
        break
    else:
      print 'That is not a valid move. Type the x digit (1-8), then the y digit (1-8).'
      print 'For example, 81 will be the top-right corner'
  print 'Valid move'
  return [x, y]

def getComputerMove(board, computerTile):
  # gien a board and computer's tile, determine where to 
  # move and return that move as a [x, y] list
  possibleMoves = getValidMoves(board, computerTile)
  # randomize the order of the possible moves
  random.shuffle(possibleMoves)
  # always go for the corner if available
  for x, y in possibleMoves:
    if isOnCorner(x, y):
      return [x, y]
  # go through all possible moves and remember best scoring move
  bestScore = -1
  for x, y in possibleMoves:
    dupeBoard = getBoardCopy(board)
    makeMove(dupeBoard, computerTile, x, y)
    score = getScoreOfBoard(dupeBoard) [computerTile]
    if score > bestScore:
      bestMove = [x, y]
      bestScore = score
  return bestMove
  
def showPoints(mainBoard, playerTile, computerTile):
  # print out current score
  scores = getScoreOfBoard(mainBoard)
  print 'You have {0} points. The computer has {1} points.'.format(scores[playerTile], scores[computerTile])
  
def main():
  while True:
    # reset the board and game
    mainBoard = getNewBoard()
    resetBoard(mainBoard)
    playerTile, computerTile = enterPlayerTile()
    print 'Player tile', playerTile
    print 'Computer tile', computerTile
    showHints = False
    turn = whoGoesFirst()
    print 'The ' + turn + ' will go first.'
  
    while True:
      if turn == 'player':
        print 'Player turn.'
        # Player's turn:
        if showHints:
          drawBoard(getBoardWithValidMoves(mainBoard, playerTile))
        else:
          drawBoard(mainBoard)
        showPoints(mainBoard, playerTile, computerTile)
        move = getPlayerMove(mainBoard, playerTile)
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
          makeMove(mainBoard, playerTile, move[0], move[1])
        if getValidMoves(mainBoard, computerTile) == []:
          print 'No valid computer moves.  Ending game.'
          break
        else:
          print 'Now computer turn.'
          turn = 'computer'
      else:
        print 'Computer turn.'
        # Computer's turn:
        drawBoard(mainBoard)
        showPoints(mainBoard, playerTile, computerTile)
        raw_input("Press enter to see the computer's move.")
        x, y = getComputerMove(mainBoard, computerTile)
        print 'Computer move:', [x + 1, y + 1]
        makeMove(mainBoard, computerTile, x, y)
      
        if getValidMoves(mainBoard, playerTile) == []:
          print 'No valid player moves.  Ending game.'
          break
        else:
          print 'Now player turn.'
          turn = 'player'
    
    # Display the final score
    drawBoard(mainBoard)
    scores = getScoreOfBoard(mainBoard)
    print 'X scored {0} points. O score {1} points'.format(scores['X'], scores['O'])
    if scores[playerTile] > scores[computerTile]:
      print 'You beat the computer by {0} points! Gratz!'.format(scores[playerTile] - scores[computerTile])
    elif scores[playerTile] < scores[computerTile]:
      print 'You lost. The computer beat you by {0} points'.format(scores[computerTile] - scores[playerTile])
    else:
      print 'The game was a tie!'
    
    if not playAgain():
      break    

if __name__ == '__main__':
  print 'Welcome to Reversi!'
  main()
