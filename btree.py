import random

def Add(tree, value):
  if not tree:
    tree.append(value)
    tree.append([])
    return tree
  tree_value = tree[0]
  if tree_value == value:
    return Add(tree[1], [value]) # creates a new brnch from this value, allowing for multiple branches
  else:
    return Add(tree[1], value)

def Print(tree, indent):  
  if not tree:
    return
  if len(str(tree[0])) == 1:
    print '    ' * indent, tree[0]
    Print(tree[1], indent + 1)
  else:
    Print (tree[0][0], indent + 1)
  return tree

def getTree(tree, word):
  for c in word:
    Add(tree, c)
  Add(tree, '*')
  return tree