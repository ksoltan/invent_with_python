import random

def Add(tree, value):
  if not tree: # If the list is empty
    tree.append(value[0])
    tree.append([])
    return Add(tree[1], value[1:])
  
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
    Add(char_tree, w)
  print char_tree

if __name__ == "__main__":
    main()
