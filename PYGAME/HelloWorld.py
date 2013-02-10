import pygame, sys
from pygame.locals import *

# Set up Pygame
pygame.init()

# Set up the window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello World!')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up fonts
basicFont = pygame.font.SysFont(None, 48)

# Set up the text
text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Draw the white background onto surface
windowSurface.fill(WHITE)
# Draw green polygon onto surface
pygame.draw.polygon(windowSurface, GREEN, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw some blue lines into surface
pygame.draw.line(windowSurface, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(windowSurface, BLUE, (120, 60), (120, 120))
pygame.draw.line(windowSurface, BLUE, (60,121),(130, 120), 4)

# Draw blue circle onto surface
pygame.draw.circle(windowSurface, BLUE, (300, 50), 20, 0)

# Draw red ellipse onto surface
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Draw text background onto surface
pygame.draw.rect(windowSurface, RED, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# Get pixel array of surface
pixArray = pygame.PixelArray(windowSurface)
pixArray[480][380] = BLACK
del pixArray

# Draw the text onto surface
windowSurface.blit(text, textRect)
# Draw the window onto the screen
pygame.display.update()

# Run the game loop
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit(0)