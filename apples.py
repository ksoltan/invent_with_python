# This is a game of chance. You get an apple which has a random number
# of seeds. Each number has a fortune.

import random
import time
import sys

print('Hello! What is your name?')
myName=input()
print('Hi '+myName+', would you like to eat an apple to find out your fortune?')
input()
def to_bool(x):# If you say yes, the program will go on to tell you your fortune.
    return str(x) in ('yes', 'true', 'y')

while True:
    print('Well, '+myName+', here is your apple fortune...')
    apple = random.randint(1, 6) #Computer randomly picks #of seeds in apple.
    time.sleep(2) #inserts time in between the displayed words.
    
    if int(apple) == 1:
        print('''You have '''+str(apple)+''' seed in your apple.''')
        time.sleep(2)
        print('''You will find your true love soon.''')

    if int(apple) == 2:
        print('''You have '''+str(apple)+''' seeds in your apple.''')
        time.sleep(2)
        print('You will have a new car in a month.')

    if int(apple) == 3:
        print('''You have '''+str(apple)+''' seeds in your apple.''')
        time.sleep(2)
        print('You will have a very nice day on Friday.')

    if int(apple) == 4:
        print('''You have '''+str(apple)+''' seeds in your apple.''')
        time.sleep(2)
        print('''Sweets are good for you. You will receive a
basket of chocolate this weekend.''')

    if int(apple) == 5:
        print('''You have '''+str(apple)+''' seeds in your apple.''')
        time.sleep(2)
        print('The flowers of your garden will bloom brightly the whole year.')

    if int(apple) == 5:
        print('''You have '''+str(apple)+''' seeds in your apple.''')
        time.sleep(2)
        print('You will win tickets to your favorite team\'s game!')

        
    time.sleep(3)
    print('Would you like to eat another apple and try your luck?')
    if not to_bool(input()):
        sys.exit(0)

