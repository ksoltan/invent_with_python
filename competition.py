# Given a string of numbers formed as follows: 1234567891011121314...  WHat is the 100th numeral?

def SequenceOfNumbers(count):
  long_str = ''
  for x in range(1, count):
    long_str += str(x)
  return long_str

# What is the 283d 7 in the sequence above?
def FindNthDigit(sequence, digit_to_find, digit_count):
  current_count = 0
  current_position = 0
  for digit in sequence:
    current_position += 1
    if digit == digit_to_find:
      current_count += 1
      if current_count == digit_count:
        return current_position
  return -1

# print "Generating digit sequence"
# x = SequenceOfNumbers(100)
# print "sequence:", x
# print "10th 7 position is", FindNthDigit(x, '7', 10)

print "Generating digit sequence"
x = SequenceOfNumbers(1000)
print "283rd 7 position is", FindNthDigit(x, '7', 283)

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
  for y in range(2, x/2 + 1):
    if x%y == 0:
      print 'divisible by:', y

def isPrime(x):
  for y in range(2, x/2 + 1):
    if x%y == 0:
      return False
  return True


