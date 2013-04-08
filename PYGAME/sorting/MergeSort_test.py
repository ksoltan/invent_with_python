from mock import MagicMock
import unittest
import pygame
import mock
import random
from MergeSort import *

class MergeSortTest(unittest.TestCase):
  def setUp(self):
    self.range = 100
    self.l = range(self.range)
    random.shuffle(self.l)
    self.sorter = MergeSort()

  def testRecursiveMergeSort(self):
    sorted_list, complexity = self.sorter.RecursiveSort(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "RecursiveSort:", complexity

class MergeSortElementAnimationTest(unittest.TestCase):
  def setUp(self):
    elem = 4
    pos = 0
    self.animation = Element(elem, pos)

  def testCtor(self):
    self.assertEqual(4, self.animation.elem)
    self.assertEqual(0, self.animation.pos)
  
  def testElementInListPosition(self):
    self.animation.getRect()
    self.assertEqual(pygame.Rect(0, 0, 1, 4), self.animation.rect)
  
  def testElementInListChangesPosistion(self):
    self.animation.changePos(1)
    self.assertEqual(1, self.animation.pos)
  
  def testElementIterationCallsGettingNewRect(self):
    self.animation.getRect = MagicMock()
    self.animation.Iteration()
    self.animation.getRect.assert_called_once_with()

  def testElementIterationCallsAnUpdateOfTheScreen(self):
    self.animation.update = MagicMock()
    self.animation.Iteration()
    self.animation.update.assert_called_once_with()
    
if __name__ == '__main__':
  unittest.main()