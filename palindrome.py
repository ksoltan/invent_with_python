# A palindromic number reads the same both forwards and backwards. For
# For instance, 22, 5445, and 17271 are all palindromes. What is the largest
# 5-digit palindrome that is a product of two 3-digit palindromes?

import copy

def IsPalindrome(num):
  num_str = str(num)
  num_list = []
  for c in num_str:
    num_list.append(c)
  num_reversed = copy.copy(num_list)
  num_reversed.reverse()
  return num_list == num_reversed

def RemoveFromRange(num_range, vals):
  for val in vals:
    if val in num_range:
      num_range.remove(val)

def ThreeDiditPalindromes():
  result = []
  for i in range(1, 10):
    for j in range(10):
      result.append(i*101 + j*10)
  return result

def main():
  pal3_1 = ThreeDiditPalindromes()
  pal3_2 = copy.copy(pal3_1)
  prods = []
  for pal1 in pal3_1:
    for pal2 in pal3_2:
      prod = pal1 * pal2
      if IsPalindrome(prod) and len(str(prod)) == 5:
        prods.append([prod, pal1, pal2])
  prods.sort(key = lambda elem: elem[0])
  print 'All prods:', prods
  print 'Head prod:', prods[:1]
  print 'Tail prod:', prods[-1:]
  
if __name__ == '__main__':
  main()
