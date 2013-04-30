import unittest
import math
from reverse_print import *

class ListTest(unittest.TestCase):
  def setUp(self):
    self.l = List()

  def testCtor(self):
    self.assertEqual(None, self.l.head)

  def testAppendToEmptyList(self):
    self.l.Append(Node(1))
    self.assertEqual(1, self.l.head.value)
    self.assertEqual(None, self.l.head.next)

  def testAppendToNonEmptyList(self):
    self.l.Append(Node(1))
    self.l.Append(Node(2))
    self.assertEqual(1, self.l.head.value)
    self.assertEqual(2, self.l.head.next.value)
    self.assertEqual(None, self.l.head.next.next)

  def testSize(self):
    self.l.Append(Node(1))
    self.assertEqual(1, self.l.Size())
    self.l.Append(Node(2))
    self.assertEqual(2, self.l.Size())

  def testGet(self):
    self.l.Append(Node(1))
    self.l.Append(Node(2))
    self.assertEqual(1, self.l.Get(0).value)
    self.assertEqual(2, self.l.Get(1).value)
    self.assertRaises(IndexError, self.l.Get, 2)
    self.assertEqual(1, self.l.Get(0).value)

  def testReversePrint(self):
    n1 = Node(1)
    self.l.Append(n1)
    self.assertEqual([n1], self.l.ReversePrint())
    n2 = Node(2)
    self.l.Append(n2)
    self.assertEqual([n2, n1], self.l.ReversePrint())

  def testPrint(self):
    n1 = Node(1)
    self.l.Append(n1)
    self.assertEqual([n1], self.l.Print())
    n2 = Node(2)
    self.l.Append(n2)
    self.assertEqual([n1, n2], self.l.Print())

if __name__ == '__main__':
    unittest.main()