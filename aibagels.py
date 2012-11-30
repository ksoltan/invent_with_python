# YOU think of a number and the computer guesses it

import random

def guessNum(num_guess):
  if raw_input().lower().startswith('y'):
    playAgain()
  else:
    random.shuffle(num_guess)
    print 'Is your number {0}?'.format(num_guess[0])
    guessNum(num_guess[1:])

def playAgain():
  print 'Do you want me to guess another number?'
  if raw_input().lower().startswith('n'):
    print 'Thank you for playing. Bye.'
  else:
    startGame()

def startGame():
  print 'Think of a number between 1 and 20. I will guess it.'
  print 'Press enter when ready.'
  guessNum(range(20))

startGame()