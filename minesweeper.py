#Trying to rewrite minesweeper.py
import random
import sys

ROWS = 5
COLUMNS = 5
MINES = 4

def newBoard():
  mines = []
  for m in range(MINES):
    mines.append(1)
  spaces =[]
  for es in range(ROWS * COLUMNS - MINES):
    spaces.append(0)
  all_spaces = mines + spaces
  random.shuffle(all_spaces)
  board = []
  for r in range(ROWS):
    row = []
    board.append(row)
    for c in range(COLUMNS):#get the index for list of all_spaces, returns item from all_spaces
      row.append(all_spaces[r * COLUMNS + c])         
  return board
    
def getMove():
  print 'Please enter your move.'
  print 'Row:'
  row = int(raw_input())
  print 'Column:'
  col = int(raw_input())
  pos = [row, col]
  return pos
  
def isValidMove(pos, tested_positions):
  if pos[0] not in range(ROWS) or pos[1] not in range(COLUMNS) or pos in tested_positions:
    # print 'Move is invalid!'
    return False
  else:
    return True

def isBomb(board, pos):
  r = pos[0]
  c = pos[1]
  return board[r][c] == 1
          
def openTrivialPositions(board, tested_positions, pos):
  if getNumMinesAt(board, pos) != 0:
    return
  row = pos[0]
  col = pos[1]
  # Cannot start from -1 as it will wrap around the board.
  start_row = max(row - 1, 0)
  start_col = max(col - 1, 0)
  for r in range(start_row, row + 2): # picks the touching cells left and right
    for c in range(start_col, col + 2): # picks the touching cells up and down
      test_pos = [r, c]
      if isValidMove(test_pos, tested_positions) and \
        test_pos not in tested_positions:
        tested_positions.append([r, c])
        openTrivialPositions(board, tested_positions, test_pos)
  
def getNumMinesAt(board, pos):
  row = pos[0]
  col = pos[1]
  # Cannot start from -1 as it will wrap around the board.
  start_row = max(row - 1, 0)
  start_col = max(col - 1, 0)
  num_mines = 0
  # Since empty spaces are 0, and bombs are 1, if we go through and add the value
  # given to the spot on the board to number of bombs, we get the number of bombs
  # around it.
  for r in board[start_row: row + 2]: # picks the touching cells left and right
    for c in r[start_col: col + 2]: # picks the touching cells up and down
      num_mines += c
  return num_mines

def showBoard(board, tested_positions):
  for r in range(len(board)):
    row = board[r]
    for c in range(len(row)):
      position = [r, c]
      if position in tested_positions:
        print getNumMinesAt(board, position),
      else:
        print '.',
    print
  
def showBombBoard(board):
  for r in range(len(board)):
    row = board[r]
    for c in range(len(row)):
      if board[r][c] == 1:
        print '*',
      else:
        print '.',
    print
  
def foundAllPositions(board, tested_positions):
  return len(tested_positions) == (ROWS * COLUMNS - MINES)
  # all_positions = []
  # for r in range(len(board)):
  #   row = board[r]
  #   for c in range(len(row)):
  #     if board[r][c] == 0:
  #       all_positions.append([r, c])
  # return tested_positions == all_positions 
    
def playAgain():
  print 'Would you like to play again? (yes o no)'
  return raw_input().lower().startswith('y')

def startGame():  
  tested_positions = []
  b = newBoard()
  showBoard(b, tested_positions)
  while True:
    print 'Tested positions:', tested_positions
    pos = getMove()
    if isValidMove(pos, tested_positions):
      tested_positions.append(pos)
    else:
      continue
    # Move is guaranteed to be valid now, check for bombs.
    if isBomb(b, pos):
      print 'You have hit a bomb!'
      print 'YOU LOSE!!!'
      showBombBoard(b)
      if playAgain():
        startGame()
      else:
        sys.exit(0)
    openTrivialPositions(b, tested_positions, pos)
    if foundAllPositions(b, tested_positions):
      if playAgain():
        startGame()
      else:
        sys.exit(0)
    else:
      showBoard(b, tested_positions)

print 'MINESWEEPER'
startGame()
