from mock import MagicMock
import unittest
import random
from list_sorter import *

# class ListSorterTest(unittest.TestCase):
#   def setUp(self):
#     self.sorter = ListSorter()
# 
#   def testRecursiveBubbleSortMin(self):
#     l = [3, 5, 1, 4, 2]
#     self.assertEqual([1, 2, 3, 4, 5], self.sorter.RecursiveBubbleSortMin(l))
# 
#   def testRecursiveBubbleSortMax(self):
#     l = [3, 5, 1, 4, 2]
#     self.assertEqual([1, 2, 3, 4, 5], self.sorter.RecursiveBubbleSortMax(l))
# 
#   def testBubbleSort(self):
#     l = [3, 5, 1, 4, 2]
#     self.assertEqual([1, 2, 3, 4, 5], self.sorter.BubbleSort(l))
# 
#   def testRecursiveMergeSort(self):
#     l = [3, 5, 1, 4, 2]
#     self.assertEqual([1, 2, 3, 4, 5], self.sorter.RecursiveMergeSort(l))

class ListSorterExtremeTest(unittest.TestCase):
  def setUp(self):
    self.range = 100
    self.l = range(self.range)
    random.shuffle(self.l)
    self.sorter = ListSorter()

  def testRecursiveBubbleSortMin(self):
    sorted_list, complexity = self.sorter.RecursiveBubbleSortMin(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "RecursiveBubbleSortMin:", complexity

  def testRecursiveBubbleSortMax(self):
    sorted_list, complexity = self.sorter.RecursiveBubbleSortMax(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "RecursiveBubbleSortMax:", complexity

  def testBubbleSort(self):
    sorted_list, complexity = self.sorter.BubbleSort(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "BubbleSort:", complexity

  def testRecursiveMergeSort(self):
    sorted_list, complexity = self.sorter.RecursiveMergeSort(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "RecursiveMergeSort:", complexity

  def testRecursiveRandomSortMin(self):
    sorted_list, complexity = self.sorter.RecursiveRandomSort(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "RecursiveRandomSort:", complexity

  def testRecursiveInsertionSort(self):
    sorted_list, complexity = self.sorter.InsertionSort(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "InsertionSort:", complexity

if __name__ == '__main__':
    unittest.main()
