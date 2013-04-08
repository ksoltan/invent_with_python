import pygame
import random
from pygame.locals import *

pygame.init()
WINDOWWIDTH = 20
WINDOWHEIGHT = 20
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Bubble Sort Animation')
mainClock = pygame.time.Clock()
BLUE = (0, 0, 255)

class Animation():
  """docstring for Animation"""
  def __init__(self, l):
    self.l = l

  def GetRects(self):
    self.anim_list = [pygame.Rect(pos * 10, 0, 1, self.l[pos]) for pos in range(len(self.l))]

  def Update(self, new_list):
    self.l = new_list

  def Display(self):
    [pygame.draw.rect(windowSurface, BLUE, rect) for rect in self.anim_list]
    pygame.display.update()

class BubbleSort():
  """docstring for BubbleSort"""
  def __init__(self):
    pass

  def RecursiveMin(self, l):
    """docstring for sort"""
    # bubble down, find the lowest element and save it
    # recursive stoping point
    if len(l) == 1:
      return (l, 0)
    # bubble down min element
    animation = Animation(l)
    animation.GetRects()
    algorithm_complexity = 0
    for i in range(1, len(l)):
      if l[0] > l[i]:
        l[0], l[i] = l[i], l[0]
        animation.Update(l)
      animation.Display()
      algorithm_complexity += 2
    # remember min
    l_min = l[:1]
    # recursively sort smaller list
    (smaller_l, recursive_complexity) = self.RecursiveMin(l[1:])
    # combine min and sorted smaller list
    return (l_min + smaller_l, algorithm_complexity + recursive_complexity)

  def RecursiveMax(self, l):
    """docstring for sort"""
    # bubble up, find the greatest element and save it
    # recursive stoping point
    if len(l) == 1:
      return (l, 0)
    # bubble up max element
    algorithm_complexity = 0
    current_max_i = 0
    for i in range(1, len(l)):
      if l[current_max_i] > l[i]:
        l[current_max_i], l[i] = l[i], l[current_max_i]
      current_max_i = i
      algorithm_complexity +=2
    # remember max
    l_max = l[-1:]
    # recursively sort smaller list
    (smaller_l, recursive_complexity) = self.RecursiveMax(l[:-1])
    # combine sorted smaller list and max
    return (smaller_l + l_max, algorithm_complexity + recursive_complexity)

  def Sort(self, l2):
    """docstring for sort2"""
    # bubble down, find the smallest element and put into the ith position
    algorithm_complexity = 0
    l = l2[:]
    for i in range(len(l)):
      for j in range(i, len(l)):
        if l[i] > l[j]:
          l[i], l[j] = l[j], l[i]
        algorithm_complexity += 2
    return l, algorithm_complexity