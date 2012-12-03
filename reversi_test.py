import reversi

board = reversi.getNewBoard()
reversi.drawBoard(board)
move = reversi.getPlayerMove(board, 'X')
print 'should return a move:', move