# This is a matching game
import random
import time

ROWS = 3
COLUMNS = 2

def getBoard(rows, columns):
  num_range = range(columns * rows / 2)
  all_nums = num_range * 2
  random.shuffle(all_nums)
  
  board = []
  for x in range(rows):
    board.append([])
    for y in range(columns):
      board[x].append(all_nums.pop())
  return board
  
def printBoard(b):
  for r in b:
    for c in r:
      print " ", c, " ",
    print
    
def isPositionInRange(positions, pos):
  return pos in positions

def showBoard(b, show_positions = [], show_all = False):
  for row in range(len(b)):
    row_values = b[row]
    for col in range(len(row_values)):
      value = "."
      if show_all:
        value = row_values[col]
      elif [row, col] in show_positions:
        value = row_values[col]
      print " ", value, " ",
    print

def getSingleCard(msg):
  print msg
  print 'row = ',
  row = int(raw_input())
  print 'col = ',
  col = int(raw_input())
  return [row, col]

def getMove():
  m1 = getSingleCard('First card:')
  m2 = getSingleCard('Second card:')
  return [m1, m2]

def getBoardValue(board, pos):
  row, col = pos[0], pos[1]
  return board[row][col]

def isGoodMove(board, positions):
  val1 = getBoardValue(board, positions[0])
  val2 = getBoardValue(board, positions[1])
  return val1 == val2

def memoryGame():
  b = getBoard(ROWS, COLUMNS)
  numMoves = 0
  goodMoves = []
  while True:
    print 'Your moves:', goodMoves
    print 'Current board:'
    showBoard(b, goodMoves)
    move = getMove()
    if isGoodMove(b, move):
      goodMoves += move
      if len(goodMoves) == ROWS * COLUMNS:
        print 'You have solved memory game.'
        print 'Final board:'
        printBoard(b)
        break
    else:
      showBoard(b, goodMoves + move)
      time.sleep(5)
      numMoves += 1





##def getMatchingPairs(rows, columns): 
##    number_pairs = rows*columns/2
##    board_of_matches = []
##    for i in range(number_pairs):
##        board_of_matches.append(i) 
##def getMatchingPairs(columns): 
##    number_pairs = 18
##    board_of_matches = []
##    for x in range(columns):
##        board_of_matches.append([])
##        for i in range(18):
##            board_of_matches.append(i)
##            board_of_matches.append(i)
##            random.shuffle(board_of_matches)
##    return board_of_matches
##def getMatchingPairs(columns):
##    board_of_matches = []
##    number_of_pairs = '012345678'*2
##    number_of_pairs.split()
##    for i in number_of_pairs:
##        board_of_matches.append(random.sample(number_of_pairs, 1))
##    return board_of_matches
def getMatchingPairs():
    pairs = '012345678'*2
    pairs.split()
    return pairs




