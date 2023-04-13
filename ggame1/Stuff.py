import pygame
import os

class Stuff():
    def __init__(self, WIDTH, HEIGHT):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        self.snd_dir = os.path.join(game_folder, 'snd')
        self.player_img = pygame.image.load(os.path.join(img_folder, 'GreenImg.png')).convert()
        self.enemy_img = pygame.image.load(os.path.join(img_folder, 'RedImg.png')).convert()
        self.bullet_img = pygame.image.load(os.path.join(img_folder, 'laserImg.png')).convert()
        self.box_img = pygame.image.load(os.path.join(img_folder, 'BoxImg.png')).convert()
        self.med_img = pygame.image.load(os.path.join(img_folder, 'MedImg.png')).convert()
        self.background = pygame.image.load(os.path.join(img_folder, 'Background.jpg')).convert()
        self.background_rect = self.background.get_rect()


class MusicStuff():
     def __init__(self, snd_dir):
        self.shoot_sound = pygame.mixer.Sound(os.path.join(snd_dir, 'shoot.wav'))
        self.score_sound = pygame.mixer.Sound(os.path.join(snd_dir, 'score.wav'))
        self.med_sound = pygame.mixer.Sound(os.path.join(snd_dir, 'med.wav'))
        self.box_sound = pygame.mixer.Sound(os.path.join(snd_dir, 'box.wav'))


class StartGame():
    def __init__(self, snd_dir):
        pygame.display.set_caption("My Game")
        pygame.mixer.music.load(os.path.join(snd_dir, 'musicex.wav'))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(loops=-1)