#Tic-Tac-Toe

import random

def drawBoard(board):
    #This function prints out board that it was passed.
    #board is a list of 10 strings representing the board(ignore index 0)
    print('   |    ')
    print(' ' + board[7] + '  |  ' + board[8] +'  |  ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    #lets player type in which symbol he wants to be
    #returns list with player's symbol as 1st item and computer's symbol as the 2nd
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    #returns True if player wants to play again.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    #returns true if plpayer has won
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))
def getBoardCopy(board):
    # Make duplicate of board list and return it the duplicate
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)
        return dupeBoard

def isSpaceFree(board, move):
    #Return true if passed move is free on the passed board
    return board[move] == ''

def getPlayerMove(board):
    #Let player type in his move
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    #Returns valid move from passed list on the passed board.
    #Returns None is there is no valid move
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

def getComputerMove(board, computerLetter):
    #Given a board and the computer's letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #Here is our first algorithm for Tic Tac Toe AI:
        #First, check if we can win in the next moce for i in range(1, 10)
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    #Check if player can win i next move, block them
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSapceFree(copy,  i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    #Try to take one of the corners, if free
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    #Try to take center if free
    if isSpaceFree(board, 5):
        return 5
    #Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    #Return True if every space on board is taken. Otherwise return False
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
        return True

print('Welcome to Tic-Tac-Toe!')

while True:
    #Reset board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The '+turn+' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Hooray! You have won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            #Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('Ha! The computer has beaten you! You Lose.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break
                        
                    
    
            













    
