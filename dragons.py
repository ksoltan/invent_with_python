# This is a dragon game. You go into a cave and you either win or die.

import random
import sys

print('If you are not asked to answer a question, please press ENTER.')
input()

def to_bool(x):
    return str(x).lower() in ('yes', 'true')

while True:
    print("""You are in a land full of dragons.
    In front of you, you see two caves. In one cave,
    the dragon is friendly and will share his treasure
    with you. The other dragon is greedy and hungry,
    and will eat you on sight.""")
    cave=random.randint(1, 2)
    print('Which cave will you go into?')
    guess=int(input())

    if guess != cave:
        print("""You approach the cave...
It is dark and spooky...
A large dragon jumps out in front of you! He opens his jaws, and...
Gobbles you down in one bite!!!""")
    
    if guess == cave:
        print('''You approach the cave...
It is dark and spooky...
A large dragon comes into view. He sees you and...
Gives you all his treasure!!!!!''')

    print('Do you want to play again? (yes or no)')
    if not to_bool(input()):
        sys.exit(0)
