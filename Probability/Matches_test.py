import random
import unittest
from Matches import *

class GameTest(unittest.TestCase):
  def setUp(self):
    self.game = Game()

  def testCtor(self):
    self.assertEqual(PEOPLE, len(self.game.matches))
    self.assertEqual(0, len(self.game.wins))
    self.assertEqual(0, len(self.game.draws))

  def testDraw(self):
    self.game.Draw()
    self.assertEqual(1, len(self.game.wins))
    self.assertEqual(1, len(self.game.draws))

  def testPlay(self):
    self.game.Play()
    self.assertEqual(PEOPLE, len(self.game.wins))
    self.assertEqual(PEOPLE, len(self.game.draws))
    self.assertEqual(NUM_LONG, self.game.wins.count(True))
    # self.game.PrintDebug()

  # def testConsequentDraws(self):
  #   self.game.Draw()
  #   self.game.Draw()
  #   self.assert_(0 <= self.game.results[1])
  #   self.assert_((len(self.game.matches)-1) >= self.game.results[1])
  #   self.assertEqual(2, len(self.game.results))
  #   self.assertNotEqual(self.game.results[0], self.game.results[1])
  #   self.game.Draw()
  #   self.assertNotEqual(self.game.results[0], self.game.results[2])
  #   self.assertNotEqual(self.game.results[1], self.game.results[2])
  #   
  # def testIteration(self):
  #   self.game.Iterate()
  #   self.assertEqual(PEOPLE, len(self.game.results))
  
  # def testPrintDebug(self):
  #   self.game.PrintDebug()
  # def testSuccessRates(self):
  #   self.game.SuccessRate__()
if __name__ == '__main__':
    unittest.main()