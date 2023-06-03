import random
import pygame

class Mob(pygame.sprite.Sprite):
    def __init__(self, params, colors, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = params.enemy_img
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(-100, -40)
        self.rect.y = random.randrange(size.HEIGHT - self.rect.height)
        self.speedx = random.randrange(3, 8)
        self.speedy = random.randrange(-2, 2)
        self.size = size

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right > self.size.WIDTH + 10 or self.rect.top < -25 or self.rect.bottom > self.size.HEIGHT + 25:
            self.rect.y = random.randrange(self.size.HEIGHT - self.rect.height)
            self.rect.x = random.randrange(-100, -40)
            self.speedx = random.randrange(3, 8)
            self.speedy = random.randrange(-2, 2)