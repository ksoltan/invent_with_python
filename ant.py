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

import copy

def GetPathWeight(path):
  """docstring for GetPathWeight"""
  weight = 0
  for step in path:
    weight += WEIGHTS[step[0]][step[1]]
  return weight
  
def FindAllPaths(paths):
  """docstring for FindAllPaths"""
  x, y = paths[0]
  right_value = x + 1
  if right_value < 5:
    paths[1].append([right_value, y])
    paths[1].append([])
    paths[1].append([])
    FindAllPaths(paths[1])
  down_value = y + 1
  if down_value < 5:
    paths[2].append([x, down_value])
    paths[2].append([])
    paths[2].append([])
    FindAllPaths(paths[2])
    
def PrintPaths(paths, indent):
  if not paths:
    return
  PrintPaths(paths[1], indent + 1)
  print '----' * indent, paths[0]
  PrintPaths(paths[2], indent + 1)
  
def PrintPathsWeights(paths, weight, weights):
  """docstring for BuildPathsFromTree"""
  x, y = paths[0]
  leaf_path = True
  if paths[1]:
    leaf_path = False
    PrintPathsWeights(paths[1], weight + WEIGHTS[x][y], weights)
  if paths[2]:
    leaf_path = False
    PrintPathsWeights(paths[2], weight + WEIGHTS[x][y], weights)
  if leaf_path:
    weights.append(weight)
    print 'Path weight:', weight

def main():
  """docstring for main"""
  paths = [[0, 0], [], []]
  FindAllPaths(paths)
  # PrintPaths(paths, 0)
  weights = []
  PrintPathsWeights(paths, 0, weights)
  weights.sort()
  print weights

if __name__ == '__main__':
  main()
