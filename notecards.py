# This let's you add notes

import sys
import flashcards

notes = []

def getNote(notes):
  print 'Would you like to enter a note?'
  if raw_input().lower().startswith('n'): # point of stop. if answer is no...
    numberNote = range(len(notes))
    printNotes(numberNote, notes)
  else:
    print 'Enter the TITLE of your note.'
    title = raw_input()
    print 'Enter your INFORMATION.'
    info = raw_input()
    notes.append([title, info])
    getNote(notes)

def printNotes(numberNote, finalNotes):
  if len(numberNote) == 0:
    testYourself(notes)
  else:
    title = finalNotes[0][0]
    info = finalNotes[0][1]
    print numberNote[0], title, info
    printNotes(numberNote[1:], finalNotes[1:])

def testYourself(notes):
  print 'Do you want to test yourself now?'
  if raw_input().lower().startswith('n'):
    print 'Bye!'
  else:
    flashcards.randomWord(notes)
getNote(notes)