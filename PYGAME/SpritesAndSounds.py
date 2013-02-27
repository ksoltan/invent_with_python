import pygame, sys, time, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Sprites and Sounds')

BLACK = (0, 0, 0)

player = pygame.Rect(300, 100, 40, 40)
playerImage = pygame.image.load('player.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
foodImage = pygame.image.load('cherry.png')
foods = []
for i in range(20):
  foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))

foodCounter = 0
NEWFOOD = 40

# Keyboard Variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 6

# Music
pickUpSound = pygame.mixer.Sound('gulp.wav')
pygame.mixer.music.load('background.mid')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit(0)
    if event.type == KEYDOWN:
      # Change the keyboard variables
      if event.key == K_LEFT or event.key == ord('a'):
        moveRight = False
        moveLeft = True
      if event.key == K_RIGHT or event.key == ord('d'):
        moveRight = True
        moveLeft = False
      if event.key == K_UP or event.key == ord('w'):
        moveDown = False
        moveUp = True
      if event.key == K_DOWN or event.key == ord('s'):
        moveDown = True
        moveUp = False
    if event.type == KEYUP:
      if event.key == K_ESCAPE:
        pygame.quit()
        sys.exit(0)
      if event.key == K_LEFT or event.key == ord('a'):
        moveLeft = False
      if event.key == K_RIGHT or event.key == ord('d'):
        moveRight = False
      if event.key == K_UP or event.key == ord('w'):
        moveUp = False
      if event.key == K_DOWN or event.key == ord('s'):
          moveDown = False
      if event.key == ord('x'):
        player.top = random.randint(0, WINDOWHEIGHT - player.height)
        player.left = random.randint(0, WINDOWWIDTH - player.width) 
      if event.key == ord('m'):
        if musicPlaying:
          pygame.mixer.music.stop()
        else:
          pygame.mixer.music.play(-1, 0.0)
        musicPlaying = not musicPlaying
  foodCounter += 1
  if foodCounter >= NEWFOOD:
    foodCounter = 0
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - 20), random.randint(0, WINDOWHEIGHT - 20), 20, 20))
  
  windowSurface.fill(BLACK)
  
  if moveDown and player.bottom < WINDOWHEIGHT:
    player.top += MOVESPEED
  elif moveUp and player.top > 0:
    player.top -= MOVESPEED
  elif moveLeft and player.left > 0:
    player.left -= MOVESPEED
  elif moveRight and player.right < WINDOWWIDTH:
    player.right += MOVESPEED
  
  windowSurface.blit(playerStretchedImage, player)
  
  for food in foods[:]:
    if player.colliderect(food):
      foods.remove(food)
      player = pygame.Rect(player.left, player.top, player.width + 2, player.height + 2)
      playerStretchedImage = pygame.transform.scale(playerImage, (player.width, player.height))
      if musicPlaying:
        pickUpSound.play()
  for food in foods:
    windowSurface.blit(foodImage, food)
    
  pygame.display.update()
  mainClock.tick(40)