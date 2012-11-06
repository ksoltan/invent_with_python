import sonar

chests = sonar.getRandomChests(3)
print 'getRandomChests(3):', chests

print 'move should be valid:', sonar.isValidMove(0, 12)
print 'move should be invalid:', sonar.isValidMove(-1, 12)
print 'move should be invalid:', sonar.isValidMove(65, 12)
print 'move should be invalid:', sonar.isValidMove(0, -1)
print 'move should be invalid:', sonar.isValidMove(0, 20)

# print 'getNewBoard()', sonar.getNewBoard()

b = sonar.getNewBoard()
print 'getRow(b,0)', sonar.getRow(b, 0)
# print 'getRow(b,1)', sonar.getRow(b, 1)

print 'drawBoard:'
sonar.drawBoard(b)

print 'Should be valid move:', sonar.makeMove(b, chests, 30, 7)
sonar.drawBoard(b)
