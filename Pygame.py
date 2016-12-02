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
            center=(random.randint(820, 900), random.randint(0, 600)))
        self.speed = random.randint(5, 10)
        

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()

pygame.init()
clock = pygame.time.Clock()
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Avoid OSU')
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
player = Player()
sound = pygame.mixer.Sound("Blue.wav")
background = pygame.image.load('Field.bmp')
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
running = True
WHITE = (255,255,255)
score = 0
timer = 0
seconds = clock.tick()/100

timer += int(seconds)
font = pygame.font.Font(None, 36)
scoretext = font.render('Player Score: '+str(score), 1, [255,0,0])
boxsize = scoretext.get_rect()
timertext = font.render('Timer: %d'%timer, 1, [255,0,0])
boxsize = timertext.get_rect()

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
    screen.blit(scoretext, (10,40))
    timertext = font.render('Timer: '+str(timer), 1, [255,0,0])
    screen.blit(timertext, (10,10))

    seconds = clock.tick()/10

    timer += int(seconds)
    



    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        pygame.quit()
        print ("Your score was "+ str(score))

        # text = font.render("Game Over", True, WHITE)
        # text_rect = text.get_rect()
        # text_x = screen.get_width() / 2 - text_rect.width / 2
        # text_y = screen.get_height() / 2 - text_rect.height / 2
        # screen.blit(text, [text_x, text_y])
        # pygame.quit()


    else:
    
        pygame.display.flip()
# pygame.quit()

