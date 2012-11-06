import random

words = 'eggs ham sausage pomegranite banana olives chicken'.split()

def random_word(wordList):
    x = random.randint(0, len(wordList)-1)
    return words[x]

print('What is your name?')
name = raw_input()
play_again = False

def say_what_you_like(name, rword):
    print(str('Hello {0}, I know that you like ' +
              'to eat {1} for breakfast, right?').format(name, rword))
    
say_what_you_like(name, random_word(words))

if raw_input() == 'yes':
    play_again = True    
