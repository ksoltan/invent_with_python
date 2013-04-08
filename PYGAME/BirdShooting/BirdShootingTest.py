import mock
import pygame
import unittest
from BirdShooting import *

class PebbleMovementTest(unittest.TestCase):
  def setUp(self):
    p = pygame.Rect(10, 5, 100, 50)
    self.peb1 = Pebble(p, UPRIGHT, 5)
    self.peb2 = Pebble(p, UPLEFT, 5)

  def testCtorOfPebble(self):
    self.assertEqual(10, self.peb1.rect.left)
    self.assertEqual(UPRIGHT, self.peb1.dir)
    self.assertEqual(5, self.peb1.speed)
  
  def testPebbleMovesUpRight(self):
    self.peb1.MoveUpRight()
    self.assertEqual(10, self.peb1.rect.top)
    self.assertEqual(5, self.peb1.rect.left)

  def testPebbleMovesUpLeft(self):
    self.peb2.MoveUpLeft()
    self.assertEqual(0, self.peb2.rect.top)
    self.assertEqual(5, self.peb2.rect.left)

class BirdMovementTest(unittest.TestCase):
  def setUp(self):
    r = pygame.Rect(10, 5, 100, 50)
    self.b1 = Bird(r, RIGHT, 5)
    self.b2 = Bird(r, LEFT, 5)

  def testCtorOfBird(self):
    self.assertEqual(10, self.b1.rect.left)
    self.assertEqual(RIGHT, self.b1.dir)
    self.assertEqual(5, self.b1.speed)

  def testBirdFliesRight(self):
    self.b1.FlyRight()
    self.assertEqual(15, self.b1.rect.left)

  def testBirdFliesLeft(self):
    self.b2.FlyLeft()
    self.assertEqual(5, self.b2.rect.left)
  
  def testBirdChangesDirectionToDownWhenHit(self):
    self.b1.IsHit()
    self.assertEqual(DOWN, self.b1.dir)
  
  def testBirdFallsDown(self):
    self.b1.FallDown()
    self.assertEqual(10, self.b1.rect.top)
#  def testBirdMovesDownWhenHit(self):
  # must know how to use mock...

class BirdAndPebbleInteractionsTest(unittest.TestCase):
  def setUp(self):
    self.b1 = Bird(pygame.Rect(10, 5, 100, 50), RIGHT, 5)
  
  def testBirdIsHitByPebble(self):
    p = Pebble(pygame.Rect(10, 5, 100, 50), UPRIGHT, 5)
    hit = self.b1.MaybeHit([p])
    self.assertEqual(True, hit)

    
if __name__ == '__main__':
    unittest.main()
