# Kind of like minesweeper

import random

ROWS = 4
COLUMNS = 4

def getBoard(rows, columns):
  num_range = range(rows * columns / 2)
  all_nums = num_range * 2
  random.shuffle(all_nums)
  for x in all_nums:
    if x == 3 or 7:
      x = 1 #a bomb
    else:
      x = 0
  board = []
  for r in range(rows):
    board.append([])
    for c in range(columns):
      board[r].append(all_nums.pop())
  return board    

def printBoard(board):
  for r in board:
    for c in board[r]:
      print ' ', c, ''
    print
def getPos():
  print 'Type in a position you would like to test:'
  print 'row:'
  row = raw_input
  print 'column'
  col = raw_input
  return [row, col]

def isPosValid([row, col]):
  
  
  
  