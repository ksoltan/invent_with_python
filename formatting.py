import random

words = 'eggs ham sausage pomegranite banana olives chicken'.split()

def random_word(wordList):
    x = random.randint(0, len(wordList)-1)
    random_word = words[x]
    return random_word

print('What is your name?')
name = input()
play_again = False

def say_what_you_like(name, random_word):
    print(''''Hello {}, I know that you like to eat {}
for breakfast, right?'''.format(name, random_word))
    
random_word(words)
say_what_you_like(name, random_word)

if input() == True:
    play_again = True    
