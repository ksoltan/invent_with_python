import memory

b = memory.getBoard(2, 3)
print 'Print board'
memory.printBoard(b)

print 'Test position in range:', memory.isPositionInRange([[0, 0], [0, 1], [1, 0], [1, 1]], [0,1])
print 'Test position in range:', memory.isPositionInRange([[0,1],[1,1],[2,3]], [0,1])
print 'Test position not in range:', memory.isPositionInRange([[0,1],[1,1],[2,3]], [0,0])
print 'Test position not in range:', memory.isPositionInRange([[0,1],[1,1],[2,3]], [0,2])
print 'Test position not in range:', memory.isPositionInRange([[0,1],[1,1],[2,3]], [1,3])

print 'Show board disclose everything:'
memory.showBoard(b, [], True)

print 'Show board hide everything:'
memory.showBoard(b, [], False)

print 'Show board with positions:'
memory.showBoard(b, [[0,0],[2,0]], False)

testBoard = [
  [0, 1, 2],
  [2, 0, 1]
]

print 'Test good move:', memory.isGoodMove(testBoard, [[0, 0],[1, 1]])
print 'Test wrong move:', memory.isGoodMove(testBoard, [[0, 0],[1, 0]])
