# Recursion: quizzes you on vocab

import random
import copy
import sys

WORDLIST = [['silicon', 'Si'], ['barium', 'Ba'], ['Tellurium', 'Te'], ['Tungsten', 'W'], ['Iodine', 'I']]
random.shuffle(wordList)

def randomWord(words):
  if not words:
    print 'Good job'
    return
  else:
    print words[0][0]
    if raw_input() == words[0][1]:
      randomWord(words[1:])
    else:
      random.shuffle(words)
      randomWord(words)
      
randomWord(WORDLIST)