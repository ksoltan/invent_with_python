import math

answers = []
for n in range(1, 100):
  insertion = 8 * (n**2)
  merge = 64 * n * (math.log(n, 2))
  if insertion <= merge:
    answers.append(n)
answers = []
for n in range(1, 100):
  if 100 * n**2 < 2**n:
    answers.append(n)
    break

print answers