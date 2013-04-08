from mock import MagicMock
import pygame
import unittest
from TurkeyShoot import *

main()

class BirdTest(unittest.TestCase):
  def setUp(self):
    self.bird = Bird(pygame.Rect(10, 5, 100, 50), RIGHT, 5)

  def testCtor(self):
    self.assertEqual(pygame.Rect(10, 5, 100, 50), self.bird.rect)
    self.assertEqual(RIGHT, self.bird.dir)
    self.assertEqual(5, self.bird.speed)

  def testChangeDirLeft(self):
    self.bird.ChangeDir()
    self.assertEqual(LEFT, self.bird.dir)

  def testChangeDirRight(self):
    self.bird.ChangeDir()
    self.bird.ChangeDir()
    self.assertEqual(RIGHT, self.bird.dir)

  def testChangeDirRaise(self):
    self.bird.dir = UP
    self.assertRaises(Exception, self.bird.ChangeDir)

  def testMoveRight(self):
    self.bird.Move()
    self.assertEqual(pygame.Rect(15, 5, 100, 50), self.bird.rect)

  def testInWindow(self):
    self.assertTrue(self.bird.IntersectRect(pygame.Rect(0, 0, 700, 700)))

  def testNotInWindow(self):
    self.assertFalse(self.bird.IntersectRect(pygame.Rect(0, 0, -700, -700)))

  def testPebbleHit(self):
    self.assertTrue(self.bird.IntersectRect(pygame.Rect(10, 5, 3, 3)))

  def testPebbleNotHit(self):
    self.assertFalse(self.bird.IntersectRect(pygame.Rect(0, 0, 3, 3)))

class TurkeyShootGameTest(unittest.TestCase):
  def setUp(self):
    """docstring for setUp"""
    self.game = TurkeyShoot(10, 5)
    self.game.TakeAim = MagicMock()
    self.game.InitCannon(6, 6)

  def testCtor(self):
    self.assertEqual(10, self.game.birds_num)
    self.assertEqual(5, self.game.pebbles_num)
    self.assertEqual(0, self.game.aim_degrees)
  
  def testBirdInitialization(self):
    self.game.bird_num = 2
    self.game.InitBirds()
    self.assertEqual([Bird(pygame.Rect(0, 0, 50, 20), RIGHT, 4)], self.game.birds)


  def testIterationNum(self):
    """Test that game has as many iterations as there are pebbles."""
    [self.game.Iterate() for i in range(5)]
    self.assertTrue(self.game.IsFinished())

  def testIterationLaunchesPebble(self):
    """Iteration should call LaunchPebble."""
    self.game.LaunchPebble = MagicMock()
    self.game.Iterate()
    self.game.LaunchPebble.assert_called_once_with()

  def testIterationGetsPebblePosition(self):
    self.game.GetPebblesPos = MagicMock()
    self.game.Iterate()
    self.game.GetPebblesPos.assert_called_once_with()
    
  def testIterationTakesAim(self):
    """Iteration should call TakeAim."""
    self.game.Iterate()
    self.game.TakeAim.assert_called_once_with()

  def testLaunchPebbleDecrementsPebbleNum(self):
    """Test that game has as many iterations as there are pebbles."""
    self.assertEqual(5, self.game.pebbles_num)
    self.game.LaunchPebble()
    self.assertEqual(4, self.game.pebbles_num)

  def testLaunchPebbleRight(self):
    self.game.pebble = pygame.Rect(50, 50, 10, 10)
    self.game.LaunchRight()
    self.assertEqual(pygame.Rect(55, 55, 10, 10), self.game.pebble)

  def testLaunchPebbleLeft(self):
    self.game.pebble = pygame.Rect(50, 50, 10, 10)
    self.game.LaunchLeft()
    self.assertEqual(pygame.Rect(45, 45, 10, 10), self.game.pebble)

  def testLaunchPebbleUp(self):
    self.game.pebble = pygame.Rect(50, 50, 10, 10)
    self.game.LaunchUp()
    self.assertEqual(pygame.Rect(50, 55, 10, 10), self.game.pebble)
  
  def testWhichPebbleDirLaunchesRight(self):
    self.game.aim_degrees = 25
    self.game.LaunchRight = MagicMock()
    self.game.WhichPebbleDirection()
    self.game.LaunchRight.assert_called_once_with()
  
  def testWhichPebbleDirLaunchesLeft(self):
    self.game.aim_degrees = -25
    self.game.LaunchLeft = MagicMock()
    self.game.WhichPebbleDirection()
    self.game.LaunchLeft.assert_called_once_with()
  
  def testWhichPebbleDirLaunchesUp(self):
    self.game.aim_degrees = 0
    self.game.LaunchUp = MagicMock()
    self.game.WhichPebbleDirection()
    self.game.LaunchUp.assert_called_once_with()

  def testAdjustAimLeft(self):
    """docstring for testAdjustAimLeft"""
    self.assertEqual(0, self.game.aim_degrees)
    self.game.AdjustAimLeft()
    self.assertEqual(-5, self.game.aim_degrees)

  def testAdjustAimRight(self):
    self.assertEqual(0, self.game.aim_degrees)
    self.game.AdjustAimRight()
    self.assertEqual(5, self.game.aim_degrees)
    
  def testAdjustAimLeftIsOutOfRange(self):
    self.game.aim_degrees = -50
    self.game.AdjustAimLeft()
    self.assertEqual(-45, self.game.aim_degrees)

  def testAdjustAimRightIsOutOfRange(self):
    self.game.aim_degrees = 135
    self.game.AdjustAimRight()
    self.assertEqual(45, self.game.aim_degrees)
  
  def testWhenGetAimShootPebble(self):
    self.game.LaunchPebble = MagicMock()
    self.game.Iterate()
    self.game.LaunchPebble.assert_called_once_with()

  def testPebbleDirectionLeft(self):
    '''The pebble will be shot left.'''
    self.game.aim_degrees = -5
    self.game.WhichPebbleDirection()
    self.assertEqual(UPLEFT, self.game.pebbles_dir)

  def testPebbleDirectionRight(self):
    '''The pebble will be shot right.'''
    self.game.aim_degrees = 5
    self.game.WhichPebbleDirection()
    self.assertEqual(UPRIGHT, self.game.pebbles_dir)

  def testPebbleDirectionUp(self):
    '''The pebble will be shot straight up.'''
    self.game.aim_degrees = 0
    self.game.WhichPebbleDirection()
    self.assertEqual(UP, self.game.pebbles_dir)
  
  def testInitializationOfCannon(self):
    self.assertEqual(pygame.Rect(3, 6, 40, 50), self.game.cannon)

  def testGetPebblePosition(self):
    self.game.cannon_image = pygame.Rect(3, 4, 40, 50)
    self.assertEqual(pygame.Rect(0, 0, 10, 10), self.game.pebble)
    self.game.GetPebblePos()
    self.assertEqual(pygame.Rect(3, 4, 10, 10), self.game.pebble)

  # def testDegreesChangePebbleDirectionLeft(self):
  #   self.game.AdjustAimLeft()
  #   self.assertEqual(pygame.transform.rotate(self.game.cannon_image, 5), self.game.cannon_image)

  # def testNewBirdIsInWindow(self):
  #   bird = self.game.LaunchPebble()
  #   self.assertTrue(bird.IntersectRect(pygame.Rect(0, 0, 700, 700)))
  # 
  # def testBirdLeavesWindow(self):
  #   bird = self.game.LaunchPebble()
  #   [bird.Move() for x in range(200)]
  #   self.assertFalse(bird.IntersectRect(pygame.Rect(0, 0, 700, 700)))

  # test that you cannot launch more birds than birds_num

if __name__ == '__main__':
    unittest.main()
