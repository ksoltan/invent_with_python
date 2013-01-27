# An ant leaves from the top left and wants to go to the bottom right
# corner. It can only move down or right. What is the minimum sum of the path
# it can take?

WEIGHTS = [
    [  0, 44, 72, 91, 47, ],
    [ 63, 50, 69, 33, 61, ],
    [ 16, 35, 84, 57, 76, ],
    [ 55, 88, 50, 35, 24, ],
    [ 48, 66, 19, 41,  0 ]
]

def FindAllPaths(paths, value):
  if len(paths) >= 8:
    return paths
  if not paths:
    paths.append(value)
    paths.append([]) # down step
    paths.append([]) # right step
    FindAllPaths(paths, value)
  else:
    x = FindIndex(value)
    if x[0] == 4 or x[1] == 4:
      return paths
    else:  
      down_value = x[0] + 1
      return FindAllPaths(paths[1], WEIGHTS[down_value][x[1]])
      right_value = x[1] + 1
      return FindAllPaths(paths[2], WEIGHTS[x[0]][right_value])

def FindIndex(value):
  for x in range(5):
    if value in WEIGHTS[x]:
      return [x, WEIGHTS[x].index(value)]    
def main():
  pass

if __name__ == '__main__':
  main()