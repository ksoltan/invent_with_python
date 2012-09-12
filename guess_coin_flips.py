# This is also a coin flip game but you must guess the number of heads.

import random
print("I will flip a coin 1000 times. Guess how many times it'll be heads!")
guess_heads = int(input())
heads = 0
flips = 0
def your_guess(x, y):
    if x == y:
        print('You are correct! Good job!')
    else:
        print('Sorry, there were actually ' + str(x) + ' heads out of 100 tosses.')

while flips < 1000:
    if random.randint(0, 1) == 1:
        heads += 1
    flips += 1

your_guess(heads, guess_heads)
