import unittest
import math
from ProblemSizeVsTime import *

class ProblemSizeVsTimeTest(unittest.TestCase):
  def setUp(self):
    self.problem = ProblemVsTime()
    self.problem.time = [1]
  
  def testCalculationOfLog(self):
    self.problem.CalculateLog(1, 1)
    self.problem.CalculateLog(1, 3)
    self.assertEqual([[2, 8],[],[],[],[],[],[],[]], self.problem.answers)

  def testCalculationOfSqrt(self):
    self.problem.CalculateSqrt(0, 1)
    self.problem.CalculateSqrt(0, 2)
    self.assertEqual([[],[1, 4],[],[],[],[],[],[]], self.problem.answers)

  def testCalculationOfLinear(self):
    self.problem.CalculateLinear(0, 2)
    self.problem.CalculateLinear(0, 6)
    self.assertEqual([[],[],[2, 6],[],[],[],[],[]], self.problem.answers)

  def testCalculationOfComplexLog(self):
    self.problem.CalculateCmplxLog(1, 2)
    self.problem.CalculateCmplxLog(1, 8)
    self.assertEqual([[],[],[],[2, 4],[],[],[],[]], self.problem.answers)

  def testCalculationOfSquare(self):
    self.problem.CalculateSquare(0, 4)
    self.problem.CalculateSquare(0, 9)
    self.assertEqual([[],[],[],[],[2, 3],[],[],[]], self.problem.answers)

  def testCalculationOfCube(self):
    self.problem.CalculateCube(0, 8)
    self.problem.CalculateCube(0, 64)
    self.assertEqual([[],[],[],[],[],[2, 4],[],[]], self.problem.answers)

  def testCalculationOfPower(self):
    self.problem.CalculatePower(0, 8)
    self.problem.CalculatePower(0, 16)
    self.assertEqual([[],[],[],[],[],[],[3, 4],[]], self.problem.answers)

  def testCalculationOfFactorial(self):
    self.problem.CalculateFactorial(0, 6)
    self.problem.CalculateFactorial(0, 24)
    self.assertEqual([[],[],[],[],[],[],[],[3, 4]], self.problem.answers)

if __name__ == '__main__':
    unittest.main()