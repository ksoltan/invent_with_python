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
RED = (128, 0, 0)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
YELLOW = (235, 235, 0)

# Set up fonts
basicFont = pygame.font.SysFont(None, 48)

# Set up the text
text = basicFont.render('Hello world!', True, WHITE, TEAL)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

# Draw the white background onto surface
windowSurface.fill(WHITE)
# Draw purple polygon onto surface
pygame.draw.polygon(windowSurface, PURPLE, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Draw some teal lines into surface
pygame.draw.line(windowSurface, TEAL, (60, 80), (140, 80), 5)
pygame.draw.line(windowSurface, TEAL, (60, 80), (60, 140), 5)
pygame.draw.line(windowSurface, TEAL, (140, 80), (140, 140), 5)
pygame.draw.line(windowSurface, TEAL, (60,140),(140, 140), 5)

# Draw TEAL circle onto surface
pygame.draw.circle(windowSurface, TEAL, (300, 50), 20, 0)

# Draw red ellipse onto surface
pygame.draw.ellipse(windowSurface, RED, (300, 250, 40, 80), 1)

# Draw text background onto surface
pygame.draw.rect(windowSurface, YELLOW, (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

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