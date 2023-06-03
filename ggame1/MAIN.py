import pygame

from Stuff import Stuff, StartGame, MusicStuff
from Player import Player
from Colors import Colors, Size
from Mob import Mob
from FallingStuff import Box, Med

FPS = 60
size = Size()
colors = Colors()
params = Stuff(size.WIDTH, size.HEIGHT)

def show_go_screen():
    params.screen.blit(params.background, params.background_rect)
    draw_text(params.screen, "THE GAME", 64, size.WIDTH / 2, size.HEIGHT / 4)
    draw_text(params.screen, "Стрелочки - движение, пробел - стрельба", 22, size.WIDTH / 2, size.HEIGHT / 2)
    draw_text(params.screen, "Нажмите пробел, чтобы играть!", 18, size.WIDTH / 2, size.HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        params.clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    waiting = False


def draw_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 50
    BAR_HEIGHT = 12
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, colors.RED, fill_rect)
    pygame.draw.rect(surf, colors.BLACK, outline_rect, 2)


font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, colors.BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


pygame.init()
StartGame(params.snd_dir)
music = MusicStuff(params.snd_dir)

game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        boxes = pygame.sprite.Group()
        meds = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        player = Player(params, colors, size)
        all_sprites.add(player)
        for i in range(5):
            m = Mob(params, colors, size)
            all_sprites.add(m)
            mobs.add(m)
        b = Box(params, size, colors)
        all_sprites.add(b)
        boxes.add(b)
        g = Med(params, size, colors)
        all_sprites.add(g)
        meds.add(g)
        SCORECOUNTER = 0
        AMMO = 100
        HP = 100
        SCORE = 0
    params.clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if AMMO > 0:
                    player.shoot(all_sprites, bullets, music)
                AMMO -= 5

    all_sprites.update()
    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        m = Mob(params, colors, size)
        all_sprites.add(m)
        mobs.add(m)
        HP -= 20
        if HP <= 0:
            game_over = True
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        SCORE += 50
        m = Mob(params, colors, size)
        all_sprites.add(m)
        mobs.add(m)
        SCORECOUNTER += 1
    hits = pygame.sprite.spritecollide(player, boxes, True)
    if hits:
        b = Box(params, size, colors)
        all_sprites.add(b)
        boxes.add(b)
        AMMO = 100
        SCORE += 100
        SCORECOUNTER += 1
        music.box_sound.play()
    hits = pygame.sprite.spritecollide(player, meds, True)
    if hits:
        g = Med(params, size, colors)
        all_sprites.add(g)
        meds.add(g)
        if HP <= 80:
            HP += 20
        music.med_sound.play()
    if SCORE % 1000 == 0 and SCORECOUNTER > 0:
        music.score_sound.play()
        SCORECOUNTER = 0

    params.screen.fill(colors.BLACK)
    params.screen.blit(params.background, params.background_rect)
    all_sprites.draw(params.screen)
    draw_text(params.screen, 'AMMO', 36, 50, 540)
    draw_bar(params.screen, 30, 580, AMMO)
    draw_text(params.screen, 'HP', 36, 190, 540)
    draw_bar(params.screen, 170, 580, HP)
    draw_text(params.screen, str(SCORE), 30, 300, 560)
    draw_text(params.screen, 'Score', 20, 300, 540)
    pygame.display.flip()

pygame.quit()
