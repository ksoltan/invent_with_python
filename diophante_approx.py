import math

def AlmostZero(num):
  """docstring for AlmostZero"""
  return math.fabs(num) < 1e-7

def CFApproximation(iterations, parts, num):
  """Continuing fraction approximation of 'num' to 'teration' digits."""
  if iterations == 0:
    return True
  whole_part = int(math.floor(num))
  parts.append(whole_part)
  residual_part = num - whole_part
  if AlmostZero(residual_part):
    # raise Exception('Only can approximate non-terminating decimals!')
    return False
  new_num = 1.0 / residual_part
  return CFApproximation(iterations - 1, parts, new_num)
  
def CFApproximation2(iterations, parts, num):
  """docstring for Approximate"""
  if iterations == 0:
    return
  parts.append(int(math.floor(num)))
  CFApproximation2(iterations - 1, parts, 1.0 / (num - parts[-1]))
  
def main():
  """docstring for main"""
  parts = []
  CFApproximation2(100, parts, math.pi)
  print 'Parts:', parts

if __name__ == '__main__':
  main()