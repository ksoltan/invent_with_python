import mox
import pygame
import unittest
from CollisionGameClasses import *
# from pygame.locals import *

class BlockCtorTest(unittest.TestCase):
  def setUp(self):
    r = pygame.Rect(10, 5, 100, 50)
    self.block = Block.InitWithRect(r, UP)

  def testCtorSetsDirection(self):
    self.assertEqual(UP, self.block.dir)
  
  def testCtorSetsRect(self):
    self.assertEqual(10, self.block.rect.left)
    self.assertEqual(5, self.block.rect.top)
    self.assertEqual(100, self.block.rect.width)
    self.assertEqual(50, self.block.rect.height)

class BlockBounceDownTest(unittest.TestCase):
  def setUp(self):
    self.rect = pygame.Rect(10, 5, 100, 50)
  
  def testBounceDownFromUp(self):
    b = Block.InitWithRect(self.rect, UP)
    b.BounceDown()
    self.assertEqual(DOWN, b.dir)

  def testBounceDownFromUpRight(self):
    b = Block.InitWithRect(self.rect, UPRIGHT)
    b.BounceDown()
    self.assertEqual(DOWNRIGHT, b.dir)

  def testBounceDownFromUpLeft(self):
    b = Block.InitWithRect(self.rect, UPLEFT)
    b.BounceDown()
    self.assertEqual(DOWNLEFT, b.dir)

  def testBounceDownFromDown(self):
    b = Block.InitWithRect(self.rect, DOWN)
    b.BounceDown()
    self.assertEqual(DOWN, b.dir)

class MoveBlockTest(unittest.TestCase):
  def setUp(self):
    self.rect = pygame.Rect(10, 5, 100, 50)

  def testMoveDoesNotChangeDirection(self):
    b = Block.InitWithRect(self.rect, DOWNLEFT)
    b.MoveBlock(3)
    self.assertEqual(DOWNLEFT, b.dir)

  def testMoveDoesNotChangeSize(self):
    b = Block.InitWithRect(self.rect, DOWNLEFT)
    b.MoveBlock(3)
    self.assertEqual(100, b.rect.width)
    self.assertEqual(50, b.rect.height)

  def testMoveDownLeft(self):
    b = Block.InitWithRect(self.rect, DOWNLEFT)
    b.MoveBlock(3)
    self.assertEqual(7, b.rect.left)
    self.assertEqual(8, b.rect.top)

  def testMoveDownLeftAtLeftBorder(self):
    b = Block.InitWithRect(pygame.Rect(1, 5, 100, 50), DOWNLEFT)
    b.MoveBlock(3)
    # We do allow left to become negative during move.
    self.assertEqual(-2, b.rect.left)
    self.assertEqual(8, b.rect.top)

  def testMoveDownRight(self):
    b = Block.InitWithRect(self.rect, DOWNRIGHT)
    b.MoveBlock(3)
    self.assertEqual(13, b.rect.left)
    self.assertEqual(8, b.rect.top)

class BlockBounceOffWallsTest(unittest.TestCase):
  def setUp(self):
    self.mox = mox.Mox()

  def tearDown(self):
    self.mox.UnsetStubs()

  def testBounceOffLeft(self):
    # Set up.
    r = pygame.Rect(-2, 5, 100, 50)
    b = Block.InitWithRect(r, UPLEFT)
    self.mox.StubOutWithMock(b, 'BounceRight')
    b.BounceRight()
    self.mox.ReplayAll()
    # Test call.
    b.BounceOffWalls()
    # Verification.
    self.mox.VerifyAll()

  def testBounceOffRight(self):
    # Set up.
    r = pygame.Rect(5, 5, 1000, 50)
    b = Block.InitWithRect(r, UPRIGHT)
    self.mox.StubOutWithMock(b, 'BounceLeft')
    b.BounceLeft()
    self.mox.ReplayAll()
    # Test call.
    b.BounceOffWalls()
    # Verification.
    self.mox.VerifyAll()

class BlockBounceOffBlockTest(unittest.TestCase):
  def setUp(self):
    self.mox = mox.Mox()

  def tearDown(self):
    self.mox.UnsetStubs()

  def testUpLeftBouncesOffRightWall(self):
    # Set up.
    w = Block.InitWithRect(pygame.Rect(5, 5, 5, 50), UP)
    b = Block.InitWithRect(pygame.Rect(5, 25, 10, 10), UPLEFT)
    self.mox.StubOutWithMock(b, 'DoesRectTouchVerticalLine')
    b.DoesRectTouchVerticalLine(pygame.Rect(10, 5, 1, 50)).AndReturn(True)
    b.DoesRectTouchVerticalLine(pygame.Rect(5, 5, 1, 50)).AndReturn(False)
    self.mox.ReplayAll()
    # Test call.
    b.BounceOffBlock(w)
    # Verification.
    self.mox.VerifyAll()
    self.assertEqual(UPRIGHT, b.dir)

class TestBlockTouchesLine(unittest.TestCase):
  def setUp(self):
    self.b = Block.InitWithRect(pygame.Rect(10, 5, 100, 50), DOWNLEFT)

  def testCtLine(self):
    line = pygame.Rect(0, 2, 1, 700)
    self.assertEqual(0, line.left)
    self.assertEqual(2, line.top)
    self.assertEqual(1, line.width)
    self.assertEqual(700, line.height)

  def testDoesNotTouchVerticalLine(self):
    vl = pygame.Rect(0, 0, 1, 700)
    touch = self.b.DoesRectTouchVerticalLine(vl)
    self.assertEqual(False, touch)

  def testDoesTouchVerticalLine(self):
    vl = pygame.Rect(10, 0, 1, 700)
    touch = self.b.DoesRectTouchVerticalLine(vl)
    self.assertEqual(True, touch)
  
  def testDoesNotTouchHorizontalLine(self):
    hl = pygame.Rect(0, 0, 600, 1)
    touch = self.b.DoesRectTouchHorizontalLine(hl)
    self.assertEqual(False, touch)

  def testDoesTouchHorizontalLine(self):
    hl = pygame.Rect(10, 5, 600, 1)
    touch = self.b.DoesRectTouchHorizontalLine(hl)
    self.assertEqual(True, touch)

if __name__ == '__main__':
  unittest.main()
  