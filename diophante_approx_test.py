import unittest
from pi_approx import *
import math

class PiApproxTest(unittest.TestCase):
  def setUp(self):
    """docstring for setUp"""
    self.parts = []
    
  def testPi1(self):
    CFApproximation(1, self.parts, math.pi)
    self.assertEqual([3], self.parts)
    
  def testPi2(self):
    CFApproximation(2, self.parts, math.pi)
    self.assertEqual([3, 7], self.parts)

  def testPi5(self):
    self.assertTrue(CFApproximation(5, self.parts, math.pi))
    self.assertEqual([3, 7, 15, 1, 292], self.parts)
    
  def testWholeNumber(self):
    # self.assertRaises(CFApproximation(2, self.parts, 3))
    self.assertFalse(CFApproximation(2, self.parts, 3))
    self.assertEqual([3], self.parts)

  def testTerminatingDecimal(self):
    # self.assertRaises(CFApproximation(5, self.parts, 3.14))
    self.assertFalse(CFApproximation(5, self.parts, 3.14))
    self.assertEqual([3, 7, 7], self.parts)

  def testPi100(self):
    CFApproximation(100, self.parts, math.pi)
    self.assertEqual([3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 3, 3, 23, 1, 1, 7, 4, 35, 1, 1, 1, 2, 3, 3, 3, 3, 1, 1, 14, 6, 4, 5, 1, 7, 1, 5, 1, 1, 3, 18, 2, 1, 2, 4, 2, 96, 2, 3, 2, 1, 1, 6, 1, 6, 2, 5, 64, 1, 2, 3, 1, 17, 5, 1, 12, 3, 2, 1, 1, 1, 1, 2, 2, 1, 4, 1, 1, 2, 2, 22, 1, 2, 1, 6, 1, 16, 1, 2, 3, 2, 4, 2, 5, 2, 3, 1, 1], self.parts)

  def testPi100_2(self):
    CFApproximation2(100, self.parts, math.pi)
    self.assertEqual([3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 3, 3, 23, 1, 1, 7, 4, 35, 1, 1, 1, 2, 3, 3, 3, 3, 1, 1, 14, 6, 4, 5, 1, 7, 1, 5, 1, 1, 3, 18, 2, 1, 2, 4, 2, 96, 2, 3, 2, 1, 1, 6, 1, 6, 2, 5, 64, 1, 2, 3, 1, 17, 5, 1, 12, 3, 2, 1, 1, 1, 1, 2, 2, 1, 4, 1, 1, 2, 2, 22, 1, 2, 1, 6, 1, 16, 1, 2, 3, 2, 4, 2, 5, 2, 3, 1, 1], self.parts)

if __name__ == '__main__':
    unittest.main()

