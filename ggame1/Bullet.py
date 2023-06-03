import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, params, colors):
        pygame.sprite.Sprite.__init__(self)
        self.image = params.bullet_img
        self.image.set_colorkey(colors.BLACK)
        self.rect = self.image.get_rect()
        self.rect.right = x
        self.rect.centery = y
        self.speedx = -10

    def update(self):
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()

