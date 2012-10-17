#This is a hangman game!

import random
HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
=========''', '''

    +---+
    |   |
    0   |
        |
        |
        |
=========''', '''

    +---+
    |   |
    0   |
    |   |
        |
        |
=========''', '''

    +---+
    |   |
    0   |
   /|   |
        |
        |
=========''', '''

    +---+
    |   |
    0   |
   /|\  |
        |
        |
=========''', '''

    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
=========''', '''

    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
=========''']

words = '''ant babook badger bear beaver camel cat clam
cobra cougar coyote crow deer dog donkey duck eagle ferret
fox frog goat goose hawk lion lizard llama mole monkey
moose mouse mule newt otter owl panda parrot pigeon python
rabbit ram rat raven rhino salmon seal shark sheep skunk
sloth snake spider stork swan tiger trout turkey
turtle weasel whale wolf wombat zebra'''.split()

def getRandomWord(wordList):
    #this function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #replace blanks with correctly guessed #
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #show the secret word with space between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    #returns the letter the player entered. This function makes sure
    #the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter only single letter.')
        elif guess in alreadyGuessed:
                print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz' :
                print('Please enter a LETTER!')
        else:
            return guess

def playAgain():
    #this function returns True si player wants to play again.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswitch('y')


print('HANGMAN')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    #let player type in letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #check if player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
                print('Yes! The secret word is"' + secretWord
                      + '"! You have won!')
                gameIsDone = True
        else:
            missedLetters = missedLetters + guess

            #check if player guessed too monay times and lost
            if len(missedLetters) == len(HANGMANPICS) - 1:
                displayBoard(HANGMANPICS, missedLetters, correctLetters,secretWord)
                print('''You have run out of guesses!\nAfter
''' + str(len(missedLetters)) + ''' missed guesses and
''' +str(len(correctLetters))+ 'correct guesses, the word was "' + secretWord + '"')
                gameIsDone = True

            #Ask player is they want to play again, if they finished
                if gameIsDone:
                    if playAgain():
                        missedLetters = ''
                        correctLetters = ''
                        gameIsDone = False
                        secretWord = getRandomWord(words)
                    else:
                        break

            
#Bug: The correct letters and the missed letters are messed up.
#Program recognizes correct letters as missed and displays board for them.

    
