# An ant leaves from the top left and wants to go to the bottom right corner. It can only move down or right. What is the minimum sum of the path it can take?

import copy
WEIGHTS = [
    [  0, 44, 72, 91, 47, ],
    [ 63, 50, 69, 33, 61, ],
    [ 16, 35, 84, 57, 76, ],
    [ 55, 88, 50, 35, 24, ],
    [ 48, 66, 19, 41,  0 ]
]

def AddStepToPath(path, stop_idx):
  """docstring for AddStepToPath"""
  last_step = path[-1]
  paths = []
  if last_step[0] < stop_idx:
    new_path = copy.copy(path)
    new_path.append([last_step[0] + 1, last_step[1]])
    paths.append(new_path)
  if last_step[1] < stop_idx:
    new_path = copy.copy(path)
    new_path.append([last_step[0], last_step[1] + 1])
    paths.append(new_path)
  return paths

def GenerateAllPaths(stop_idx):
  """docstring for main"""
  start_path = [[0,0]]
  paths = [start_path]
  i = 0
  while True:
    print 'Iteration:', i
    i += 1
    new_paths = []
    for path in paths:
      new_paths += AddStepToPath(path, stop_idx)
    if not new_paths:
      break
    else:
      paths = new_paths
    # Debug output
    #for path in paths:
    #  print path
  return paths

def CalculatePathWeight(path):
  """docstring for CalculatePathWeights"""
  sum_weights = 0
  for step in path:
    sum_weights += WEIGHTS[step[0]][step[1]]
  return [sum_weights, path]

def main(stop_idx):
  """docstring for main"""
  paths = GenerateAllPaths(stop_idx)
  path_sums = []
  for path in paths:
    path_sums.append(CalculatePathWeight(path))
  path_sums.sort(key = lambda elem: elem[1])
  print 'The least weighted path is:', min(path_sums)
  print 'The most weighted path is:', max(path_sums)

if __name__ == '__main__':
  main(4)