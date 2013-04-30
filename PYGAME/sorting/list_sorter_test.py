from mock import MagicMock
import unittest
import random
from list_sorter import *

class ListSorterExtremeTest(unittest.TestCase):
  def setUp(self):
    self.range = 200
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

  def testInsertionSort(self):
    sorted_list, complexity = self.sorter.InsertionSort(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "InsertionSort:", complexity

  def testRecursiveInsertionSort(self):
    # sorted_list, complexity = self.sorter.RecursiveInsertionSort([3, 4, 1, 2])
    # self.assertEqual([1, 2, 3, 4], sorted_list)
    # print "RecursiveInsertionSort:", complexity
    sorted_list, complexity = self.sorter.RecursiveInsertionSort(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "RecursiveInsertionSort:", complexity
  
  def testRecursiveQuicksort(self):
    sorted_list, complexity = self.sorter.RecursiveQuicksort(self.l)
    self.assertEqual(range(self.range), sorted_list)
    print "RecursiveQuicksort:", complexity

if __name__ == '__main__':
    unittest.main()
