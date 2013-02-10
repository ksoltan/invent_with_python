import copy

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
    for path in paths:
      print path
  return paths

def main(stop_idx):
  """docstring for main"""
  paths = GenerateAllPaths(stop_idx)
  for path in paths:
    print path

if __name__ == '__main__':
  main(4)