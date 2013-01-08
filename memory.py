# This is a matching game
import random
import time
import sys

class Memory:
  def __init__(self, rows, cols):
    # save number of rows and columns
    self.rows = rows
    self.cols = cols
    # generate board: generate all numbers and fill in self.board
    num_range = range(cols * rows / 2)
    all_nums = num_range * 2
    random.shuffle(all_nums)
    self.board = []
    for x in range(rows):
      self.board.append([])
      for y in range(cols):
        self.board[x].append(all_nums.pop())
  
  def showBoard(self, show_positions = [], show_all = False):
    for row in range(len(self.board)):
      row_values = self.board[row]
      for col in range(len(row_values)):
        value = "."
        if show_all:
          value = row_values[col]
        elif [row, col] in show_positions:  
          value = row_values[col]
        print " ", value, " ",
      print

  def getSingleCard(self, msg):
    print msg
    print 'row = ',
    row = int(raw_input())
    print 'col = ',
    col = int(raw_input())
    return [row, col]

  def getMove(self):
    m1 = self.getSingleCard('First card:')
    m2 = self.getSingleCard('Second card:')
    return [m1, m2]

  def getBoardValue(self, pos):
    row, col = pos[0], pos[1]
    return self.board[row][col]

  def isGoodMove(self, positions):
    val1 = self.getBoardValue(positions[0])
    val2 = self.getBoardValue(positions[1])
    return val1 == val2
  
  def playAgain(self):
    print 'Do you want to play again?'
    return raw_input().lower().startswith('y')

  def play(self):
    numMoves = 0
    goodMoves = []
    while True:
      print 'Your moves:', goodMoves
      print 'Current board:'
      self.showBoard(goodMoves)
      move = self.getMove()
      if self.isGoodMove(move):
        goodMoves += move
        if len(goodMoves) == self.rows * self.cols:
          print 'You have solved the memory game.'
          print 'Final board:'
          self.showBoard(show_all = True)
          if self.playAgain():
            Memory(2, 3).play()
          else:
            sys.exit(0)
      else:
        self.showBoard(goodMoves + move)
        time.sleep(3)
        numMoves += 1

if __name__ == '__main__':
  print 'Welcome to memory game. Enter the coordinates!'
  while True:
    Memory(2, 3).play()
