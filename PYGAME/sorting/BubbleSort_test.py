from mock import MagicMock
import unittest
import random
import pygame
from BubbleSort import *

class BubbleSortTest(unittest.TestCase):
  def setUp(self):
    self.range = 100
    self.l = range(self.range)
    random.shuffle(self.l)
    self.sorter = BubbleSort()

  def testRecursiveBubbleSortMin(self):
    sorted_list, complexity = self.sorter.RecursiveMin(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "RecursiveBubbleSortMin:", complexity

  def testRecursiveBubbleSortMax(self):
    sorted_list, complexity = self.sorter.RecursiveMax(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "RecursiveBubbleSortMax:", complexity

  def testBubbleSort(self):
    sorted_list, complexity = self.sorter.Sort(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "BubbleSort:", complexity

class AnimationTest(unittest.TestCase):
  def setUp(self):
    rectangles = Animation(range(2))

  def testCtorOfRectangles(self):
    rectangles.GetRects()
    self.assertEqual([pygame.Rect(0, 0, 1, 0), pygame.Rect(10, 0, 1, 20)], rectangles.anim_list)

  def testUpdateList(self):
    '''Update the positions of the list being sorted.'''
    rectangles.Update(range(5))
    self.assertTrue(range(5), rectangles.l)

if __name__ == '__main__':
  unittest.main()