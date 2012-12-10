# Trees made by recursion
import sys

__TREELEN__ = 10

def getLadder(x): # ladder lik tree
  if x > TREELEN:
    print
  else:
    # print ' ' * TREELEN / 2,
    for r in range(x):
      print r,
    print
    getLadder(x+1)

getLadder(1)

def getTree(y):
  if y > __TREELEN__:
    print
  else:
    space = ((__TREELEN__ - y) / 2) * '  '
    print space,
    for r in range(y):
      print '|', # or print r to print the actual numbers.
    print
    getTree(y + 2)

getTree(1)
