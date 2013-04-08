# In this game, the player will launch pebbles at flying
# birds to knock them down from the sky. They will use the
# arrow keys to move the pebble cannon's aim and press the
# space key to shoot at the bird.
import random
import time
import pygame
from pygame.locals import *

class Pebble():
  '''Pebbles have a rectangle base, move upleft and upright
  toward the birds'''
  def __init__(self, rect, direction, speed):
    self.rect = rect
    self.dir = direction
    self.speed = speed
    self.peb_image = pygame.image.load('pebble.jpg')
  
  def MoveUpLeft(self):
    self.rect.top -= self.speed
    self.rect.left -= self.speed
  
  def MoveUpRight(self):
    self.rect.top += self.speed
    self.rect.left -= self.speed
  
  def Move(self):
    if self.dir == UPLEFT:
      self.MoveUpLeft()
    else:
      self.MoveUpRight()

  def Draw(self):
    self.windowSurface.blit(self.peb_image, self.rect)

class Bird():
  '''A bird has a rectangular base, can move either right or
  left or fall down if hit by a pebble.'''
  def __init__(self, rect, direction, speed):
    self.rect = rect
    self.dir = direction
    self.speed = speed

  def FlyRight(self):
    self.rect.left += self.speed
  
  def FlyLeft(self):
    self.rect.left -= self.speed
  
  def MaybeHit(self, pebbles):
    for p in pebbles:
      if self.rect.colliderect(p.rect):
        return True
    return False
  
  def IsHit(self):
    self.dir = DOWN
    self.FallDown()

  def FallDown(self):
    self.rect.top += self.speed

class SlingShot():
  '''A slingshot has a rectangular base, is moved by the player to determine what direction and from what position the pebbles will be shot from.'''
  def __init__(self, rect):
    self.rect = rect

pygame.init()
WINDOWWIDTH = 700
WINDOWHEIGHT = 500
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Bird Shooting')

UPLEFT = 7
UPRIGHT = 9
RIGHT = 6
LEFT = 4
DOWN = 2