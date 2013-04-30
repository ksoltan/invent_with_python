
class Node():
  """docstring for ListNode"""
  def __init__(self, value):
    self.value = value
    self.next = None
    
class List():
  def __init__(self):
    """docstring for __init__"""
    self.head = None
    
  def Append(self, node):
    node.next = None
    # If the head is empty ([])
    # the node will become the head ([node])
    if not self.head:
      self.head = node
    # If the head isn't empty, check for a next value
    # until the next value = None. Then make the next
    # value the node being appended (add reference)
    else:
      current_node = self.head
      while current_node.next:
        current_node = current_node.next
      current_node.next = node

  def Size(self):
    length = 0
    # While there is a next value, length will increase
    current_node = self.head
    while current_node:
      length += 1
      current_node = current_node.next
    return length
    
  def Get(self, idx):
    current_node = self.head
    while idx > 0:
      if current_node.next:
        current_node = current_node.next
      # Elsem there is no such index in the list
      else:
        raise IndexError()
      idx -= 1
    return current_node
  
  def Print(self):
    if not self.head:
      return
    length = self.Size()
    idx = length - 1
    while idx >= 0:
      print self.head.Get(idx)
      idx -= 1

class ReversePrinter():
  """docstring for ReversePrint"""
  def __init__(self, l):
    self.l = l
  
  def Print(self):
    self.__Print2(self.l)
    print
  
  # Recursive print
  def __Print1(self, l):
    if not l:
      return
    x = l[-1]
    # print x,
    self.__Print(l[:-1])

  def __Print2(self, l):
    for i in range(len(l)):
      x = l[-i - 1]
      # print x,

def main():
  """docstring for main"""
  p = ReversePrinter(range(10**6))
  p.Print()

if __name__ == '__main__':
  main()