
def print_rf(x): # forward recursion
  if not x: # point of stop
    print
    return
  else:
    print x[0] # small subtask
    print_rf(x[1:]) # recursive call on reduced task

print_rf(range(9))

def printBackr(x): # backward recursion
  if not x:
    print
    return
  else:
    print x[-1] #wraps right around 
    printBackr(x[:-1])

printBackr(range(9))

def printMaxr(x):# maximum recursion
  if not x:
    print
    return
  else:
    print max(x)
    printMaxr(x[:max(x)])
    
printMaxr(range(9))

def printMinr(x): # minimum recursion
  if not x:
    print
    return
  else:
    print min(x)
    printMinr(x[1:]) # the minimum is the 0th term, so pass a list omitting it.

printMinr(range(8))