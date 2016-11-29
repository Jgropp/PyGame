<<<<<<< HEAD

import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

pygame.init()
screen = pygame.display.set_mode((800, 600))
player = Player()
running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.type == QUIT:
                running = False

    screen.blit(player.surf, (400, 300))
    pygame.display.flip()
    
=======
import sys, pygame, random 

highScore = 0

# The current score during a particular round.
currentScore = 0 

# Speed of the paddle
paddleSpeed = 6

# Boolean state to tell if the game is still running or not
running = True 
# Boolean state to tell if the player has lost the game
gameLost = False
# Boolean state to tell if the player has won the game
gameWon = False

size = width, height = 500, 500 

EndGame = height - 10 

blue = 0, 0, 255 
red = 255, 0, 0 
yellow = 255, 255, 0 
green = 0, 255, 0 
white = 255, 255, 255 

circleRadius = 12 

brickPosList = [] 
brickPosList.append((50, 100)) 
brickPosList.append((200, 100)) 
brickPosList.append((350, 100)) 
brickPosList.append((50, 200)) 
brickPosList.append((200, 200)) 
<<<<<<< HEAD
brickPosList.append((350, 200)) 

class Ball:
    def __init__(self, radius, colour):
        self.radius = radius 
        self.colour = colour 
        self.centreX = 0 
        self.centreY = 0 
        self.speedX = 0 
        self.speedY = 0 

        
  def setRandomSpeed(self):
        speedRange = range(-4, 4)  
        self.speedX = random.choice(speedRange) 
        self.speedY = random.choice(speedRange) 
>>>>>>> 50850e54e9f06871de6b43d9832de1a5bd27331f
