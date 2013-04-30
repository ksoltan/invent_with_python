import random
import unittest
from GoatAndCar import *

class GameTest(unittest.TestCase):
  def setUp(self):
    self.game = Game(False)

  def testGameCtor(self):
    self.assertEqual(False, self.game.strategy)
    self.assertEqual(3, len(self.game.doors))
    self.assertEqual(2, self.game.doors.count(0))
    self.assertEqual(1, self.game.doors.count(1))
    self.assertEqual(-1, self.game.firstIndex)
    self.assertEqual(-1, self.game.secondIndex)
    self.assertEqual(-1, self.game.thirdIndex)

  def testFirstStep(self):
    self.game.FirstStep()
    self.assert_(0 <= self.game.firstIndex)
    self.assert_(self.game.firstIndex <= 2)

  def testSecondStep(self):
    self.game.FirstStep()
    self.game.SecondStep()
    self.assertNotEqual(self.game.firstIndex, self.game.secondIndex)
    self.assert_(0 <= self.game.secondIndex)
    self.assert_(self.game.secondIndex <= 2)

  def testThirdStepStrategyChange(self):
    self.game = Game(True)
    self.game.Play()
    self.assertNotEqual(self.game.firstIndex, self.game.thirdIndex)
    self.assertNotEqual(self.game.secondIndex, self.game.thirdIndex)
    self.assert_(0 <= self.game.thirdIndex)
    self.assert_(self.game.thirdIndex <= 2)

  def testThirdStepStrategyKeep(self):
    self.game = Game(False)
    self.game.Play()
    self.assertEqual(self.game.firstIndex, self.game.thirdIndex)

  # def __StrategySuccessRate(self, strategy, strategy_name):
  #   iter_num = 10000
  #   success_total = 0.0
  #   for i in range(iter_num):
  #     if Game(strategy).Play().Won():
  #       success_total += 1
  #   success_rate = (success_total / iter_num) * 100
  #   print "Strategy {0} success rate: {1}%".format(strategy_name, success_rate)
  # 
  # def testStrategyChangeSuccessRate(self):
  #   self.__StrategySuccessRate(True, 'change')
  # 
  # def testStrategyKeepSuccessRate(self):
  #   self.__StrategySuccessRate(False, 'keep')
  
  def testStrategyKeepSuccessRate(self):
    self.game.StrategySuccessRate()

  def testStrategyChangeSuccessRate(self):
    game = Game(True)
    game.StrategySuccessRate()
  # 
  # def testPrintStrategyChange(self):
  #   [Game(True).Play().PrintDebug() for i in range(10)]
  # 
  # def testPrintStrategyKeep(self):
  #   [Game(False).PrintDebug() for i in range(10)]

if __name__ == '__main__':
    unittest.main()
