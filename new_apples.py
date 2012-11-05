# This is a game of chance. You get an apple which has a random number
# of seeds. Each number has a fortune.

import random
import time
import sys

appleFortune = ['You will find your true love soon.',
'''You will have a new car in a month.''',
'''You will have a very nice day on Friday.''',
'''Sweets are good for you. You will receive a
basket of chocolate this weekend.''',
'''The flowers of your garden will bloom brightly the whole year.''',
'''You will win tickets to your favorite team\'s game!''']

def getApple(appleFortune):
    print('Well, %s, here is your apple fortune...' % myName)
    appleSeeds = random.randint(0, len(appleFortune) - 1) #Computer randomly picks #of seeds in apple.
    time.sleep(2) #inserts time in between the displayed words.
    print('You have %s apple seeds in your apple.' % appleSeeds)
    time.sleep(3)
    print('%s' % appleFortune[appleSeeds])

def PlayAgain():
    time.sleep(2)
    print('Would you like to eat another apple? (yes or no)')
    if input().lower().startswith('y'):
        getApple(appleFortune)
        PlayAgain()
    else:
        sys.exit()
        
playAgain = False
print('Hello! What is your name?')
myName=input()
print('Hi %s, would you like to eat an apple to find out your fortune?' % myName)
if input() == 'yes':
    getApple(appleFortune)
    PlayAgain()

    
