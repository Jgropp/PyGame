import pygame
import random
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('M.bmp')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('OSU.bmp')
        self.image.set_colorkey((255, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(
            center=(random.randint(820, 900), random.randint(0, 580)))
        self.speed = random.randint(5, 10)
        

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
#Initializes Pygame
pygame.init()
#Initializes Clock
clock = pygame.time.Clock()
#Creates Display
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
#Creates name of Pygame
pygame.display.set_caption('Avoid OSU')
#Adds User Event to add enemies to the game
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
#Initializes Player
player = Player()
#Creates sound
sound = pygame.mixer.Sound("Blue.wav")
#Makes picture of football field the background
background = pygame.image.load('Field.bmp')
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
running = True
WHITE = (255,255,255)
score = 0
#Creates font
font = pygame.font.Font(None, 36)
#Creates text and score counter 
scoretext = font.render('Player Score: '+str(score), 1, [255,0,0])
boxsize = scoretext.get_rect()


while running:
    sound.play()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == ADDENEMY:
            score += 1
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    screen.blit(background, (0, 0))
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)
    enemies.update()
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    scoretext = font.render('Player Score: '+str(score), 2, [255,0,0])
    screen.blit(scoretext, (300,10))
    

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        pygame.quit()
        print ("Your score was "+ str(score))

    else:
        pygame.display.flip()