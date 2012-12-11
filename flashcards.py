# Recursion: quizzes you on vocab

import random

WORDLIST = [['Adonde', 'to where'], ['Que', 'what'], ['Donde', 'where'], ['Quienes', 'whom'], ['Por que', 'why'],
['Cuando', 'when'], ['Como', 'how'], ['Cuanto', 'how much'], ['Quien', 'who'], ['Cuantos/Cuantas', 'how many']]
random.shuffle(WORDLIST)

def randomWord(words):
  if not words:
    print 'bye'
    return
  else:
    print words[0][0]
    if raw_input().lower() == words[0][1]:
      print 'Good job...'
      randomWord(words[1:])
    else:
      random.shuffle(words)
      randomWord(words)
      
randomWord(WORDLIST)