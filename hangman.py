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

words = {'colors':'''red orange yellow green blue indigo violet white
black brown emerald'''.split(), 'animals':'''ant babook badger bear beaver
camel cat clam cobra cougar coyote crow deer dog donkey duck eagle
ferret fox frog goat goose hawk lion lizard llama mole monkey moose
mouse mule newt otter owl panda parrot pigeon python rabbit ram rat
raven rhino salmon seal shark sheep skunk sloth snake spider stork
swan tiger trout turkey turtle weasel whale wolf wombat zebra'''.split(),
'fruits':'''apple orange lemon lime pear watermelon grape grapefruit
cherry banana cantalope mango strawberry'''.split()}

def getRandomWord(wordDict):
    #this function returns a random string from the passed dictionary of lists
    #of strings and the key also.
    #First randomly select a word from list of dictionaries:
    wordKey = random.choice(list(wordDict.keys()))
    #Second randomly select word from lists in dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)
    return [wordDict[wordKey][wordIndex], wordKey]

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
        guess = input().lower()
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
    return input().lower().startswith('y')


print('HANGMAN')
missedLetters = ''
correctLetters = ''
secretWord, secretKey = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is from the set of ' +secretKey)
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
            print('Yes! The secret word is' + secretWord+ '! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

    #check if player guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
##            print('''You have run out of guesses!\nAfter
##''' + str(len(missedLetters)) + ''' missed guesses and
##''' +str(len(correctLetters))+ 'correct guesses, the word was "' + secretWord + '"')
            print('''You have run out of guesses!\nAfter %s missed guesses
and %s correct guesses, the word was %s.''' % (missedLetters, correctLetters, secretWord))
            gameIsDone = True

    #Ask player is they want to play again, if they finished
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord, secretKey = getRandomWord(words)
            else:
                break
