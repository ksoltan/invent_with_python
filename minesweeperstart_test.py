import minesweeper

def printBoard(board):
  for row in board:
    for col in row:
      print col,
    print

b1 = minesweeper.getBoard(4, 4, 3)
print 'Generated board 4x4 with 3 bombs:'
printBoard(b1)

b2 = [
  [0, 1, 0],
  [0, 0, 0],
  [1, 0, 0]
]
print 'Test board 3x3 with 2 bombs:'
printBoard(b2)

print 'Show test board with no moves'
minesweeper.showBoard(b2, [])

print 'Get num mines on test board at (0, 0)'
print minesweeper.getNumMines(b2, [0, 0])

print 'Get num mines on test board at (1,1)'
print minesweeper.getNumMines(b2, [1, 1])

print 'Get num mines on test board at (2, 2)'
print minesweeper.getNumMines(b2, [2, 2])

print 'Show test board with moves: (0,0), (1,1), (2,2)'
minesweeper.showBoard(b2, [[0, 0], [1, 1], [2, 2]])

all_positions = []
for r in range(len(b2)):
  row = b2[r]
  for c in range(len(row)):
    all_positions.append([r,c])
print 'Show test board with all cells'
minesweeper.showBoard(b2, all_positions)

print 'Mine at (0, 0):', minesweeper.isMine(b2, [0, 0])
print 'Mine at (1, 1):', minesweeper.isMine(b2, [1, 1])
print 'Mine at (2, 0):', minesweeper.isMine(b2, [2, 0])
