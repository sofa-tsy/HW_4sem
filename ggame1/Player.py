import pygame
from Bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, params, colors, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = params.player_img
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (360, 240)
        self.speedx = 0
        self.speedy = 0
        self.params = params
        self.colors = colors
        self.size = size

    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        if keystate[pygame.K_UP]:
            self.speedy = -8
        if keystate[pygame.K_DOWN]:
            self.speedy = 8
        self.rect.x += self.speedx
        if self.rect.right > self.size.WIDTH:
            self.rect.right = 480
        if self.rect.bottom > self.size.HEIGHT:
            self.rect.bottom = 480
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        self.rect.y += self.speedy

    def shoot(self, all_sprites, bullets, music):
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.params, self.colors)
        all_sprites.add(bullet)
        bullets.add(bullet)
        music.shoot_sound.play()

