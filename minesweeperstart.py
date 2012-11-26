# Kind of like minesweeper

import random
import sys

ROWS = 4
COLUMNS = 4

def getBoard(rows, columns, num_mines):
  mines = []
  for b in range(num_mines):
    mines.append(1)
  empty_spaces = []
  for es in range(rows * columns - num_mines):
    empty_spaces.append(0)
  all_cells = mines + empty_spaces
  random.shuffle(all_cells)
  board = []
  for r in range(rows):
    row = []
    board.append(row)
    for c in range(columns):
      row.append(all_cells[r * columns + c])
  return board

def showBoard(board, testedPositions):
  for r in range(len(board)):
    row = board[r]
    for c in range(len(row)):
      pos = [r,c]
      if pos in testedPositions:
        print getNumMines(board, pos),
      else:
        print '.',
    print

def getNumMines(board, pos):
  row = pos[0]
  col = pos[1]
  start_row = max(row - 1, 0)
  start_col = max(col - 1, 0)
  numMines = 0
  if isMine(board, pos):
    print 'You have hit a bomb. YOU LOSE'
    sys.exit(0)
  else:
    for r in board[start_row:row + 2]:
      for c in r[start_col:col + 2]:
        numMines += c
  return numMines

def isMine(board, pos):
  r = pos[0]
  c = pos[1]
  return board[r][c] == 1

def getPos():
  print 'Type in a position you would like to test:'
  print 'row:'
  row = int(raw_input())
  print 'column:'
  col = int(raw_input())
  return [row, col]

def isPosValid(pos):
  pass
