import minesweeper

# print 'Move should be invalid: !, 8', minesweeperr.isMoveValid(['!', 8], [[0, 0], [0, 1]])
#tested_positions = []
#b = minesweeperr.getBoard()
#minesweeperr.showBoard(b, tested_positions)
#while True:
 # pos = minesweeperr.getMove() 
#  minesweeperr.isMoveValid(pos, tested_positions) 
#  minesweeperr.isBomb(b, pos) 
#  minesweeperr.getNumMines(b, pos) 
#  minesweeperr.showBoard(b, tested_positions)

#bo = [[1, 0, 0], [0, 0, 0], [0, 1, 0]]
#tested_positions = [[0, 0]]
#print 'Returns False:', minesweeperr.FoundAllPositions(bo, tested_positions)

#b = minesweeperr.getBoard()
#bd = [[1, 0, 0, 0],[0, 0, 1, 0],[0, 0, 0, 0],[1, 0, 0, 0]]
#print 'Returns a random list of 1 and 0, the board', b

#tested_positions = [[0, 1],[1, 0],[3, 3]]
#print 'Should return board.', minesweeperr.showBoard(bd, tested_positions)
#tested_positions = [[0, 1],[1, 0],[3, 3],[0, 0]]
#print 'Should return board.', minesweeperr.showBoard(bd, tested_positions)

#print 'Says how many mines are around the place (0, 0): hit bomb', minesweeperr.getNumMines(bd, [0, 0])
#print 'Says how many mines are around the place (2, 3): 1', minesweeperr.getNumMines(bd, [2, 3])

#print 'Returns True for (0, 1)', minesweeperr.isMoveValid([0, 1])
#print 'Returns True for (3, 3)', minesweeperr.isMoveValid([3, 3])
#print 'Returns False for (0, 4)', minesweeperr.isMoveValid([0, 4])

#print 'Returns a position: (0, 1)', minesweeperr.getMove()

bo = [[1, 0], [0, 1]]
print 'foundAllPositions False:', minesweeper.foundAllPositions(bo, [[0, 1]])
print 'foundAllPositions True:', minesweeper.foundAllPositions(bo,
  [[0, 1], [1, 0]])
