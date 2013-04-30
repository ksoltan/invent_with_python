import math
second = 10**6
minute = 60 * second
hour = 60 * minute
day = 24 * hour
month = 30 * day
year = 12 * month
century = 100 * year

class ProblemVsTime():
  def __init__(self):
    self.time =[second, minute, hour, day, month, year, century]
    self.answers = [[], [], [], [], [], [], [], []]

  def CalculateLog(self, n, t):
    # f(n) = log (n)
    if math.log(n, 2) == t or math.log(n, 2) > t:
      self.answers[0].append(n)
      print self.answers[0]
    else:
      self.CalculateLog(n + 1, t)
  
  def CalculateSqrt(self, n, t):
    # f(n) = sqrt(n)
    if math.sqrt(n) == t or math.sqrt(n) > t:
      self.answers[1].append(n)
      print self.answers[1]
    else:
      self.CalculateSqrt(n + 1, t)

  def CalculateLinear(self, n, t):
    # f(n) = n
    if n == t or n > t:
      self.answers[2].append(n)
      print self.answers[2]
    else:
      self.CalculateLinear(n + 1, t)

  def CalculateCmplxLog(self, n, t):
    # f(n) = n log(n)
    if n * math.log(n, 2) == t or n * math.log(n, 2) > t:
      self.answers[3].append(n)
      print self.answers[3]
    else:
      self.CalculateCmplxLog(n+1, t)

  def CalculateSquare(self, n, t):
    # f(n) = n**2
    if n**2 == t or n**2 > t:
      self.answers[4].append(n)
      print self.answers[4]
    else:
      self.CalculateSquare(n+1, t)

  def CalculateCube(self, n, t):
    # f(n) = n**3
    if n**3 == t or n**3 > t:
      self.answers[5].append(n)
      print self.answers[5]
    else:
      self.CalculateCube(n+1, t)

  def CalculatePower(self, n, t):
    # f(n) = 2**n
    if 2**n == t or 2**n > t:
      self.answers[6].append(n)
      print self.answers[6]
    else:
      self.CalculatePower(n+1, t)

  def CalculateFactorial(self, n, t):
    # f(n) = n!
    if math.factorial(n) == t or math.factorial(n) > t:
      self.answers[7].append(n)
      print self.answers[7]
    else:
      self.CalculateFactorial(n+1, t)

def main():
  problem = ProblemVsTime()
  [problem.CalculateLog(10**3, t) for t in problem.time]
  
if __name__ == '__main__':
  main()