import pygame
import random
import sys
from pygame.locals import *

class Bird():
  """docstring for Bird"""
  def __init__(self, rect, direction, speed):
    #super(Bird, self).__init__()
    self.rect = rect
    self.dir = direction
    self.speed = speed
    
  def ChangeDir(self):
    if self.dir == RIGHT:
      self.dir = LEFT
    elif self.dir == LEFT:
      self.dir = RIGHT
    else:
      raise Exception('wrong direction')

  def Move(self):
    """docstring for fname"""
    if self.dir == RIGHT:
      self.rect.left += self.speed
    elif self.dir == LEFT:
      self.rect.left -= self.speed
    else:
      raise Exception('wrong direction')

  def IntersectRect(self, rect):
    return self.rect.colliderect(rect)

class TurkeyShoot():
  """docstring for TurkeyShoot"""
  def __init__(self, birds_num, pebbles_num):
    # super(TurkeyShoot, self).__init__()
    self.birds_num = birds_num
    self.pebbles_num = pebbles_num
    self.aim_degrees = 0
    self.pebbles_dir = None
    self.pebble = pygame.Rect(0, 0, 10, 10)
    self.pebbles = []
    self.InitBirds()

  def InitBirds(self):
    bird_direction = [RIGHT, LEFT]
    bird_start = [0, WINDOWWIDTH]
    bird_left = bird_start[random.randint(0, 1)]
    if bird_left == 0:
      bird_dir = RIGHT
    else:
      bird_dir = LEFT
    self.birds = []
    self.birds.append(Bird(pygame.Rect(bird_left, 0, 50, 20), bird_dir, random.randint(4, 6)))
    self.bird_image = pygame.image.load('goose.jpg')
    self.bird_image = pygame.transform.scale(self.bird_image, (50, 50))
  
  def InitCannon(self, width, height):
    self.cannon = pygame.Rect((width / 2), (height), 40, 50)
    self.cannon_image = pygame.image.load('cannon.jpg')

  def Iterate(self):
    """docstring for fname"""
    if len(self.birds) == 0:
      self.InitBirds()
    for b in self.birds:
      for p in self.pebbles:
        if b.IntersectRect(self.pebble):
          self.birds.remove(b)
          self.pebbles.remove(p)
    if self.TakeAim():
      self.LaunchPebble()
      self.GetPebblePos()
    [p.LaunchPebble() for p in self.pebbles]
    [b.Move() for b in self.birds]
    
    [pygame.draw.rect(windowSurface, WHITE, p.rect) for p in self.pebbles]
    [windowSurface.blit(self.bird_image, b.rect) for b in self.birds]
    windowSurface.blit(self.cannon_image, self.cannon)
    pygame.display.update()
    mainClock.tick(10)

  def AdjustAimLeft(self):
    """docstring for AdjustAimLeft"""
    if self.aim_degrees <= -45:
      self.aim_degrees = -45
    else:
      self.aim_degrees -= 5
      self.cannon_image = pygame.transform.rotate(self.cannon_image, 5)
    
  def AdjustAimRight(self):
    """docstring for AdjustAimRight"""
    if self.aim_degrees >= 45:
      self.aim_degrees = 45
    else:
      self.aim_degrees += 5
      self.cannon_image = pygame.transform.rotate(self.cannon_image, -5)
  
  def StopAdjustingAim(self):
    return self.aim_degrees, self.cannon_image
    
  def GetPebblePos(self):
    self.pebble = pygame.Rect(self.cannon_image.left, self.cannon_image.top, 10, 10)
    self.pebbles.append(self.pebble)

  def TakeAim(self):
    """docstring for LaunchPebble"""
    got_aim = False
    while not got_aim:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit(0)
        if event.type == pygame.KEYDOWN:
          # Change the keyboard variables
          if event.key == pygame.K_LEFT or event.key == ord('a'):
            self.AdjustAimLeft()
          elif event.key == pygame.K_RIGHT or event.key == ord('d'):
            self.AdjustAimRight()
          elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
            print "Got Aim!"
            self.pebbles_num -= 1
            return got_aim
        elif event.type == pygame.KEYUP:
          # Change the keyboard variables
          if event.key == pygame.K_LEFT or event.key == ord('a'):
            pass
          elif event.key == pygame.K_RIGHT or event.key == ord('d'):
            pass

  def LaunchPebble(self):
    """docstring for LaunchPebble"""
    if self.aim_degrees < 0:
      self.pebbles_dir = UPLEFT
      self.LaunchLeft()
    elif self.aim_degrees > 0:
      self.pebbles_dir = UPRIGHT
      self.LaunchRight()
    elif self.aim_degrees == 0:
      self.pebbles_dir = UP
      self.LaunchUp()

  # def WhichPebbleDirection(self):
  #   if self.aim_degrees < 0:
  #     self.pebbles_dir = UPLEFT
  #     self.LaunchLeft()
  #   elif self.aim_degrees > 0:
  #     self.pebbles_dir = UPRIGHT
  #     self.LaunchRight()
  #   elif self.aim_degrees == 0:
  #     self.pebbles_dir = UP
  #     self.LaunchUp()

  def LaunchRight(self):
    self.pebble.left += 5
    self.pebble.top += 5

  def LaunchLeft(self):
    self.pebble.left -= 5
    self.pebble.top -= 5

  def LaunchUp(self):
    self.pebble.top += 5

  def IsFinished(self):
    """docstring for fname"""
    return self.pebbles_num == 0 or self.birds_num == 0


def main():
  """docstring for main"""
  game = TurkeyShoot(10, 10)
  game.InitCannon(WINDOWWIDTH, WINDOWHEIGHT)
  while True:
    windowSurface.fill(BLACK)
    if game.IsFinished():
      pygame.quit()
      sys.exit(0)
    game.TakeAim()
    game.Iterate()

pygame.init()
WINDOWHEIGHT = 700
WINDOWWIDTH = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Turkey Shoot')
mainClock = pygame.time.Clock()
UPLEFT = 7
UPRIGHT = 9
RIGHT = 6
UP = 8
LEFT = 4
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)

if __name__ == '__main__':
  main()
  