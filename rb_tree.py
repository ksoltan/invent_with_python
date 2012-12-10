import random

# Node format: [value, left, right]

def Add(tree, value):
  # Stopping point for recursion
  if not tree:
    tree.append(value)
    tree.append([])
    tree.append([])
    return tree

  tree_value = tree[0]
  if tree_value == value:
    return tree
  else:
    if tree_value < value:
      return Add(tree[2], value)
    else:
      return Add(tree[1], value)
      
def Print(tree, indent):
  # Stopping point for recursion
  if not tree:
    return

  Print(tree[2], indent + 1)
  print '    ' * indent, tree[0]
  Print(tree[1], indent + 1)

def main():
  words = '''ant antelope babook badger bear beaver camel cat clam
cobra cougar coyote crow deer dog donkey duck eagle ferret
fox frog goat goose hawk lion lizard llama mole monkey
moose mouse mule newt otter owl panda parrot pigeon python
rabbit ram rat raven rhino salmon seal shark sheep skunk
sloth snake spider stork swan tiger trout turkey
turtle weasel whale wolf wombat zebra'''.split()
  char_tree = []
  for w in words:
    print 'Adding', w
    for c in w:
      Add(char_tree, c)
  Print(char_tree, 0)

if __name__ == "__main__":
    main()

# TODO:
# 1. turn this into dictionary
# 2. Print dictionary
# 3. Add method "is given word in dictionary?"
# 4. Return completion list for a given prefix
# 5. Read http://docs.python.org/2/tutorial/classes.html
# 6. Read the rest of http://docs.python.org/2/tutorial/
