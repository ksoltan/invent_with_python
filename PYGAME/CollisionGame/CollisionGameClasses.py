import pygame, sys, random, time, math, copy
from pygame.locals import *

class Block():
  """docstring for Block"""
  def __init__(self, rect, direction):
    #super(Block, self).__init__()
    self.rect = rect
    self.dir = direction

  @staticmethod
  def InitWithRect(rect, direction):
    return Block(rect, direction)
    
  @staticmethod  
  def InitWithBounds(x_range, y_range, size, direction):
    x = random.randint(0, x_range)
    y = random.randint(0, y_range)
    return Block(pygame.Rect(x, y, size, size + 10), direction)

  def BounceDown(self):
    """docstring for BounceDown"""
    if self.dir == UPLEFT:
      self.dir = DOWNLEFT
    elif self.dir == UPRIGHT:
      self.dir = DOWNRIGHT
    elif self.dir == UP:
      self.dir = DOWN

  def BounceUp(self):
    """docstring for BounceUp"""
    if self.dir == DOWNLEFT:
      self.dir = UPLEFT
    if self.dir == DOWNRIGHT:
      self.dir = UPRIGHT
    if self.dir == DOWN:
      self.dir = UP

  def BounceRight(self):
    """docstring for BounceRight"""
    if self.dir == DOWNLEFT:
      self.dir = DOWNRIGHT
    if self.dir == UPLEFT:
      self.dir = UPRIGHT
    if self.dir == LEFT:
      self.dir = RIGHT

  def BounceLeft(self):
    """docstring for BonceLeft"""
    if self.dir == DOWNRIGHT:
      self.dir = DOWNLEFT
    if self.dir == UPRIGHT:
      self.dir = UPLEFT
    if self.dir == RIGHT:
      self.dir = LEFT

  def MoveBlock(self, speed):
    """docstring for MoveBlock"""
    if self.dir == DOWNLEFT:
      self.rect.left -= speed
      self.rect.top += speed
    if self.dir == DOWNRIGHT:
      self.rect.left += speed
      self.rect.top += speed
    if self.dir == UPLEFT:
      self.rect.left -= speed
      self.rect.top -= speed
    if self.dir == UPRIGHT:
      self.rect.left += speed
      self.rect.top -= speed
    if self.dir == UP:
      self.rect.top -= speed
    if self.dir == DOWN:
      self.rect.top += speed
    if self.dir == RIGHT:
      self.rect.left += speed
    if self.dir == LEFT:
      self.rect.left -= speed

  def BounceOffWalls(self):
    """docstring for BounceOffWalls"""
    if self.rect.top < 0:
      # block has moved past the top
      self.BounceDown()

    if self.rect.bottom > WINDOWHEIGHT:
      # block has moved past the bottom
      self.BounceUp()
      
    if self.rect.left < 0:
      # block has moved passed the left side
      self.BounceRight()
    
    if self.rect.right > WINDOWWIDTH:
      # block has moved passed the right side
      self.BounceLeft()

  def DoesRectTouchVerticalLine(self, vl):
    """docstring for doRectanglesOverlap"""
    b = self.rect
    if vl.right < b.left or b.right < vl.left:
      return False
    elif vl.top > b.bottom or b.top > vl.bottom:
      return False
    else:
      return True

  def DoesRectTouchHorizontalLine(self, hl):
    """docstring for doRectanglesOverlap"""
    b = self.rect
    if hl.top > b.bottom or b.top > hl.bottom:
      return False
    elif hl.right < b.left or b.right < hl.left:
      return False
    else:
      return True

  def BounceOffBlock(self, wall):
    """docstring for BounceOffBlock"""
    br = self.rect
    w = wall.rect
    wl = pygame.Rect(w.left, w.top, 1, w.height)
    wr = pygame.Rect(w.right, w.top, 1, w.height)
    wt = pygame.Rect(w.left, w.top, w.width, 1)
    wb = pygame.Rect(w.left, w.bottom, w.width, 1)
    if self.dir == UPLEFT:
      if self.DoesRectTouchVerticalLine(wr):
        self.dir = UPRIGHT
      elif self.DoesRectTouchHorizontalLine(wb):
        self.dir = DOWNLEFT

    if self.dir == UPRIGHT:
      if self.DoesRectTouchVerticalLine(wl):
        self.dir = UPLEFT
      elif self.DoesRectTouchHorizontalLine(wb):
        self.dir = DOWNRIGHT

    if self.dir == DOWNLEFT:
      if self.DoesRectTouchVerticalLine(wr):
        self.dir = DOWNRIGHT
      elif self.DoesRectTouchHorizontalLine(wt):
        self.dir = UPLEFT

    if self.dir == DOWNRIGHT:
      if self.DoesRectTouchVerticalLine(wl):
        self.dir = DOWNLEFT
      elif self.DoesRectTouchHorizontalLine(wt):
        self.dir = UPRIGHT

  def BlockIteration(self, windowSurface, walls, speed):
    """BlockIteration moves block one step further,
    bounces it off wals and draws on the surface."""
    self.MoveBlock(speed)
    self.BounceOffWalls()
    [self.BounceOffBlock(w) for w in walls]
    pygame.draw.rect(windowSurface, GREEN, self.rect)
    
  def WallIteration(self, windowSurface, evil_speed):
    """BlockIteration moves block one step further,
    bounces it off wals and draws on the surface."""
    self.MoveBlock(evil_speed)
    self.BounceOffWalls()
    pygame.draw.rect(windowSurface, RED, self.rect)

class Player():
  """docstring for Player"""
  def __init__(self, windowSurface, rect):
    #super(Player, self).__init__()
    self.windowSurface = windowSurface
    self.rect = rect
    self.moveRight = False
    self.moveLeft = False
    self.moveDown = False
    self.moveUp = False
    self.current_player_image = playerBiteRight
    
  def StartMoveLeft(self):
    """docstring for MovePlayerLeft"""
    self.moveRight = False
    self.moveLeft = True
    self.current_player_image = playerBiteLeft
    
  def StartMoveRight(self):
    """docstring for MovePlayerRight"""
    self.moveRight = True
    self.moveLeft = False
    self.current_player_image = playerBiteRight

  def StartMoveUp(self):
    """docstring for MovePlayerUp"""
    self.moveDown = False
    self.moveUp = True
    self.current_player_image = playerBiteUp

  def StartMoveDown(self):
    """docstring for MovePlayerDown"""
    self.moveDown = True
    self.moveUp = False
    self.current_player_image = playerBiteDown

  def StopMoveLeft(self):
    """docstring for MovePlayerLeft"""
    self.moveLeft = False
  
  def StopMoveRight(self):
    """docstring for MovePlayerRight"""
    self.moveRight = False
  
  def StopMoveUp(self):
    """docstring for MovePlayerUp"""
    self.moveUp = False
  
  def StopMoveDown(self):
    """docstring for MovePlayerDown"""
    self.moveDown = False

  def PlayerMove(self, speed):
    if self.moveDown and self.rect.bottom < WINDOWHEIGHT:
      self.rect.top += speed
    elif self.moveUp and self.rect.top > 0:
      self.rect.top -= speed
    elif self.moveLeft and self.rect.left > 0:
      self.rect.left -= speed
    elif self.moveRight and self.rect.right < WINDOWWIDTH:
      self.rect.right += speed
    self.windowSurface.blit(self.current_player_image, self.rect)

class Text():
  """docstring for Text"""
  def __init__(self, message, windowSurface):
    #super(Text, self).__init__()
    self.message = message
    self.windowSurface = windowSurface
    self.message_box = self.message.get_rect()
    self.message_box.centerx = self.windowSurface.get_rect().centerx
    self.message_box.centery = self.windowSurface.get_rect().centery
  
  def Display(self):
    self.windowSurface.blit(self.message, self.message_box)

class Game():
  """docstring for Game"""
  def __init__(self, windowSurface, food_blocks, evil_blocks, player_rect):
    #super(Game, self).__init__()
    self.food_blocks = food_blocks[:]
    self.evil_blocks = evil_blocks[:]
    self.player_rect_orig = player_rect
    self.windowSurface = windowSurface
    self.level = 1
    self.evil_speed = 3
    self.food_speed = 5
    self.food_eaten = 0
    self.player = Player(self.windowSurface, self.player_rect_orig)
    self.Messages()
    
  def Messages(self):
    self.lose_text = Text(basicFont.render('YOU LOSE!', True, RED), self.windowSurface)
    self.win_text = Text(basicFont.render('YOU WIN!', True, WHITE), self.windowSurface)

  def Iteration(self):
    self.windowSurface.fill(BLACK)
    [e.WallIteration(self.windowSurface, self.evil_speed) for e in self.evil_blocks]
    self.player.PlayerMove(self.food_speed)
    if self.AllFoodEaten():
      if self.level == 4:
        self.win_text.Display()
        self.Finish()
      self.LevelUp(direction)
    [f.BlockIteration(self.windowSurface, self.evil_blocks, self.food_speed) for f in self.food_blocks[:]]
    self.MaybeEatFood()
    self.DrawFoodEaten()
    if self.CollidesWithEvil():
      self.lose_text.Display()
      self.Finish()
    pygame.display.update()
    mainClock.tick(40)
    
  def Finish(self):
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit(0)
  
  def LevelUp(self, direction):
    self.level += 1
    level_up_text = Text(basicFont.render('LEVEL {0}'.format(self.level), True, WHITE), self.windowSurface)
    level_up_text.Display()
    pygame.display.update()
    time.sleep(2)
    for i in range(FOODNUMBER):
      d = direction[random.randint(0, 3)]
      self.food_blocks.append(Block.InitWithBounds(x_range, y_range, FOODSIZE, d))
    self.evil_speed += 0.5
    self.food_eaten = 0
    pygame.display.update()

  def CollidesWithEvil(self):
    '''If the player bumps into evil red block, the game is lost.'''
    for e in self.evil_blocks:
      if self.player.rect.colliderect(e.rect):
        return True
    return False

  def AllFoodEaten(self):
    '''Returns True if all food is eaten, False otherwise.'''
    return not self.food_blocks

  def MaybeEatFood(self):
    ate_some_food = False
    for f in self.food_blocks[:]:
      if self.player.rect.colliderect(f.rect):
        self.EatFoodBlock(f)
        ate_some_food = True
    return ate_some_food

  def EatFoodBlock(self, food_block):
    """Eats one food block."""
    self.food_blocks.remove(food_block)
    self.food_eaten += 1
    pickUpSound.play()
    self.windowSurface.blit(playerStretchedImageBite, self.player.rect)

  def DrawFoodEaten(self):
    food_text = basicFont.render('{0}'.format(self.food_eaten), True, WHITE)
    food_textRect = food_text.get_rect()
    self.windowSurface.blit(food_text, food_textRect)


pygame.init()
WINDOWWIDTH = 700
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Food and Evil: LEVEL 1')
mainClock = pygame.time.Clock()

# Direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9
DOWN = 2
UP = 8
RIGHT = 6
LEFT = 4
direction = [DOWNLEFT, DOWNRIGHT, UPLEFT, UPRIGHT]

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Music
pickUpSound = pygame.mixer.Sound('gulp.wav')
pygame.mixer.music.load('chase.wav')
pygame.mixer.music.play(-1, 0.0)

# Food Data structure
FOODNUMBER = 10
FOODSIZE = 20
food_blocks = []
x_range = WINDOWWIDTH - FOODSIZE
y_range = WINDOWHEIGHT - FOODSIZE
for i in range(FOODNUMBER):
  d = direction[random.randint(0, 3)]
  food_blocks.append(Block.InitWithBounds(x_range, y_range, FOODSIZE, d))

# Evil red block
evil1 = Block(pygame.Rect(100, 40, 40, 50), UPRIGHT)
evil2 = Block(pygame.Rect(50, 400, 40, 50), UPLEFT)
evil3 = Block(pygame.Rect(100, 37, 40, 50), DOWNLEFT)
evil4 = Block(pygame.Rect(15, 490, 40, 50), DOWNRIGHT)
evil5 = Block(pygame.Rect(100, 30, 40, 50), RIGHT)
evil6 = Block(pygame.Rect(200, 490, 40, 50), DOWNRIGHT)
evil_blocks = [evil1, evil2, evil3, evil4, evil5, evil6]

# Player
playerRect = pygame.Rect(300, 100, 50, 50)
playerImage = pygame.image.load('yellowcircle2.png')
playerImageBite = pygame.image.load('yellowbitecircle2.png')
playerStretchedImage = pygame.transform.scale(playerImage, (50, 50))
playerStretchedImageBite = pygame.transform.scale(playerImageBite, (50, 50))
playerBiteRight = playerStretchedImageBite
playerBiteUp = pygame.transform.rotate(playerBiteRight, 90)
playerBiteLeft = pygame.transform.rotate(playerBiteUp, 90)
playerBiteDown = pygame.transform.rotate(playerBiteLeft, 90)

# Text
basicFont = pygame.font.SysFont(None, 48)
# win_text = basicFont.render('YOU WIN!', True, WHITE)
# win_textRect = win_text.get_rect()
# win_textRect.centerx = windowSurface.get_rect().centerx
# win_textRect.centery = windowSurface.get_rect().centery
# lose_text = basicFont.render('YOU LOSE!', True, RED)
# lose_textRect = lose_text.get_rect()
# lose_textRect.centerx = windowSurface.get_rect().centerx
# lose_textRect.centery = windowSurface.get_rect().centery

def main():
  """docstring for main"""
  game = Game(windowSurface, food_blocks, evil_blocks, playerRect)
  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit(0)
      if event.type == KEYDOWN:
        # Change the keyboard variables
        if event.key == K_LEFT or event.key == ord('a'):
          game.player.StartMoveLeft()
        if event.key == K_RIGHT or event.key == ord('d'):
          game.player.StartMoveRight()
        if event.key == K_UP or event.key == ord('w'):
          game.player.StartMoveUp()
        if event.key == K_DOWN or event.key == ord('s'):
          game.player.StartMoveDown()
      if event.type == KEYUP:
        if event.key == K_ESCAPE:
          pygame.quit()
          sys.exit(0)
        if event.key == K_LEFT or event.key == ord('a'):
          game.player.StopMoveLeft()
        if event.key == K_RIGHT or event.key == ord('d'):
          game.player.StopMoveRight()
        if event.key == K_UP or event.key == ord('w'):
          game.player.StopMoveUp()
        if event.key == K_DOWN or event.key == ord('s'):
          game.player.StopMoveDown()
    game.Iteration()

if __name__ == '__main__':
  main()
