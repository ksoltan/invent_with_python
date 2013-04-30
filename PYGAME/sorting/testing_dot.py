import pygame
import random
from BubbleSort import *
from pygame.locals import *
import time

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Animation():
  """docstring for Animation"""
  def __init__(self):
    pass

  def GetRects(self):
    self.anim_list = [pygame.Rect((i + self.indent) * 10, 0, 2, self.l[i] * 10) for i in range(len(self.l))]

  def Display(self, new_list, indent):
    self.l = new_list
    self.indent = indent
    self.GetRects()
    pygame.draw.rect(windowSurface,
                     BLACK,
                     pygame.Rect(self.indent * 10, 0,
                                 len(self.l) * 10, max(self.l) * 10))
    [pygame.draw.rect(windowSurface, BLUE, rect) for rect in self.anim_list]
    pygame.display.update()
    # time.sleep(0.1)

class BubbleSort():
  """docstring for BubbleSort"""
  def __init__(self):
    self.animation = Animation()

  def RecursiveMin(self, l, indent):
    """docstring for sort"""
    # bubble down, find the lowest element and save it
    # recursive stoping point
    if len(l) == 1:
      return (l, 0)
    # bubble down min element
    algorithm_complexity = 0
    for i in range(1, len(l)):
      if l[0] > l[i]:
        l[0], l[i] = l[i], l[0]
        self.animation.Display(l, indent)
      algorithm_complexity += 2
    # remember min
    l_min = l[:1]
    # recursively sort smaller list
    (smaller_l, recursive_complexity) = self.RecursiveMin(
        l[1:], indent + 1)
    # combine min and sorted smaller list
    return (l_min + smaller_l, algorithm_complexity + recursive_complexity)

  def RecursiveRandomSort(self, l, indent):
    # Recursive stopping point
    if len(l) == 1:
      return (l, 0)

    # Divide task into random number subtasks
    division = random.randint(1, len(l)-1)
    l1 = l[:division]
    l2 = l[division:]

    l1_sorted, l1_complexity = self.RecursiveRandomSort(l1, indent)
    l2_sorted, l2_complexity = self.RecursiveRandomSort(l2, indent + division)

    # merge results
    algorithm_complexity = 0
    l_sorted = []
    x = 0
    y = 0
    while True:
      algorithm_complexity += 2
      if l1_sorted[x] < l2_sorted[y]:
        l_sorted.append(l1_sorted[x])
        self.animation.Display(l_sorted, indent)
  
        x += 1
        if x >= len(l1_sorted):
          l_sorted += l2_sorted[y:]
          self.animation.Display(l_sorted, indent)
          break
      else:
        l_sorted.append(l2_sorted[y])
        y += 1
        self.animation.Display(l_sorted, indent)
        if y >= len(l2_sorted):
          l_sorted += l1_sorted[x:]
          self.animation.Display(l_sorted, indent)
          break
    return (l_sorted, algorithm_complexity + l1_complexity + l2_complexity)

  def RecursiveMergeSort(self, l, indent):
    """docstring for sort2"""
    # recursive stopping point
    if len(l) == 1:
      return (l, 0)

    # divide task in smaller subtasks
    half_size = len(l)/2
    l1 = l[:half_size]
    l2 = l[half_size:]
    # and recursively sort them
    l1_sorted, l1_complexity = self.RecursiveMergeSort(l1, indent)
    l2_sorted, l2_complexity = self.RecursiveMergeSort(l2, indent + half_size)

    # merge results
    algorithm_complexity = 0
    l_sorted = []
    x = 0
    y = 0
    while True:
      algorithm_complexity += 2
      if l1_sorted[x] < l2_sorted[y]:
        l_sorted.append(l1_sorted[x])
        self.animation.Display(l_sorted, indent)
        x += 1
        if x >= len(l1_sorted):
          l_sorted += l2_sorted[y:]
          self.animation.Display(l_sorted, indent)
          break
      else:
        l_sorted.append(l2_sorted[y])
        self.animation.Display(l_sorted, indent)
        y += 1
        if y >= len(l2_sorted):
          l_sorted += l1_sorted[x:]
          self.animation.Display(l_sorted, indent)
          break
    return (l_sorted, algorithm_complexity + l1_complexity + l2_complexity)

  def BubbleSort(self, l2):
    """docstring for sort"""
    algorithm_complexity = 0
    l = l2[:]
    for i in range(len(l)):
      for j in range(i, len(l)):
        if l[i] > l[j]:
          l[i], l[j] = l[j], l[i]
          self.animation.Display(l, 0)
        algorithm_complexity += 2
    return l, algorithm_complexity

  def InsertionSort(self, l):
    algorithm_complexity = 0
    for i in range(len(l)):
      val = l[i]
      # j is the element before i which i will be compared to
      j = i - 1
      while j >= 0 and val < l[j]:
        # If the value is less than j, change j's index to the value's,
        # switching their spots.
        # Pick the next j value which is one less than the previous j.
        algorithm_complexity += 2
        l[j + 1] = l[j]
        self.animation.Display(l, 0)
        j -= 1
      # When the value is greater than j, return its position to be just after j
      l[j + 1] = val
      self.animation.Display(l, 0)
    return l , algorithm_complexity

  def RecursiveQuicksort(self, l, indent):
    if len(l) <= 1:
      return l
    pivot = random.randint(0, len(l) - 1)
    less = []
    greater = []
    for i in l:
      if i <= l[pivot]:
        less.append(i)
        self.animation.Display(less, indent)
      else:
        greater.append(i)
        self.animation.Display(greater, len(less))
    l_less = self.RecursiveQuicksort(less, indent)
    l_greater = self.RecursiveQuicksort(greater, indent + len(l_less))

    return l_less + l_greater

def GenerateListToSort():
  """docstring for Generate"""
  l = range(50)
  random.shuffle(l)
  return l

def main():
  list_being_sorted = GenerateListToSort()
  pygame.init()
  WINDOWWIDTH = len(list_being_sorted) * 10
  WINDOWHEIGHT = max(list_being_sorted) * 10
  windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
  pygame.display.set_caption('Bubble Sort Animation')
  mainClock = pygame.time.Clock()
  sorter = BubbleSort()
  #animation = Animation(list_being_sorted)
  sorter.animation.Display(list_being_sorted, 0)
  sorter.RecursiveQuicksort(list_being_sorted, 0)
  time.sleep(3)
if __name__ == '__main__':
  main()