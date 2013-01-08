# Given a string of numbers formed as follows: 1234567891011121314...  WHat is the 100th numeral?

def fibonacci():
  sequence = range(10000)
  y = ''
  for x in sequence[1:]:
    y += str(x)
  return y

# What is the 283d 7 in the sequence above?
def compute():
  z = main()
  numbers = []
  for x in range(10000):
    if z[x] == str(7):
      numbers.append([x, '7'])
  print numbers
  return numbers

# What is the 15th term of a new Fibonacci Sequence starting from 4 and 7?
#fibonacci = [4, 7]
#def Sequence(fibonacci):
#  l = len(fibonacci)
#  if l >= 16:
#    print fibonacci
#    return
#  else:
#    new_term = fibonacci[0] + fibonacci[1]
#    fibonacci.append(new_term)
#    y = l-2
#    Sequence(fibonacci[:y])

def isDivisible(x):
  numbers = range(x)
  lists = numbers[2:]
  for y in lists:
    num = int(y)
    ans = x/num
    check = ans * num
    if check == x:
      print 'divisible by:', num
      

