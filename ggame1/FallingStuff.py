import pygame
import random

class Box(pygame.sprite.Sprite):
    def __init__(self, params, size, colors):
        pygame.sprite.Sprite.__init__(self)
        self.image = params.box_img
        self.image.set_colorkey(colors.WHITE)
        self.rect = self.image.get_rect()
        t = random.randrange(1, 3)
        if t == 1:
            self.rect.x = random.randrange(size.WIDTH - self.rect.width)
        else:
            self.rect.x = random.randrange(1000, 1200)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3, 5)
        self.size = size

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > self.size.HEIGHT + 10:
            t = random.randrange(1, 3)
            if t == 1:
                self.rect.x = random.randrange(self.size.WIDTH - self.rect.width)
            else:
                self.rect.x = random.randrange(1000, 1200)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 5)


class Med(pygame.sprite.Sprite):
    def __init__(self, params, size, colors):
        pygame.sprite.Sprite.__init__(self)
        self.image = params.med_img
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        h = random.randrange(1, 5)
        if h == 1:
            self.rect.x = random.randrange(size.WIDTH - self.rect.width)
        else:
            self.rect.x = random.randrange(1000, 1200)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(3, 5)
        self.size = size

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > self.size.HEIGHT + 10:
            h = random.randrange(1, 5)
            if h == 1:
                self.rect.x = random.randrange(self.size.WIDTH - self.rect.width)
            else:
                self.rect.x = random.randrange(1000, 1200)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(3, 5)

