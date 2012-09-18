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

words = '''and babook badger bear beaver camel cat clam
cobra cougar coyote crow deer dog donkey duck eagle ferret
fox frog goat goose hawk lion lizard llama mole monkey
moose mouse mule newt otter owl panda parrot pigeon python
rabbit ram rat raven rhino salmon seal shark sheep skunk
sloth snake spider stork swan tiger trout turkey
turtle weasel whale wolf wombat zebra''' .split()

def getRandomWord(wordList):
    #this function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    
