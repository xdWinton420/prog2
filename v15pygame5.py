# 2023-04-12 Animera karaktärerna och ljud

import pygame
from sys import exit    # importerar specifikt exit-funktionen i sys-biblioteket


def display_score():
    current_time = (int)((pygame.time.get_ticks() - start_time) / 1000)      # get-ticks ger antal millisekunder efter init
    # print(current_time)
    score_surface = font.render("Score: " + (str)(current_time), False, (126, 149, 156))
    score_rectangle = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rectangle)


pygame.init()       # Startar upp pygame

screen = pygame.display.set_mode((800, 400))    # storlek på fönstret
pygame.display.set_caption("V11 Animering")     # sätter titel på fönstret
clock = pygame.time.Clock()                     # obs, stort C i Clock
game_active = True
font = pygame.font.Font("../../../Downloads/Pixeltype.ttf", 50)
start_time = 0

bg_surface = pygame.image.load("graphics/sky.png").convert()
ground_surface = pygame.image.load("graphics/ground.png").convert()
sound_bg = pygame.mixer.Sound("audio/music.wav")
sound_bg.set_volume(0.3)
sound_bg.play(loops = -1)   # loopar oändigt många gånger

# snail
snail_move1 = pygame.image.load("graphics/snail1.png").convert_alpha()
snail_move2 = pygame.image.load("graphics/snail2.png").convert_alpha()
snail_move = [snail_move1, snail_move2]
snail_index = 0
snail_surface = snail_move[snail_index]
snail_rectangle = snail_surface.get_rect(midbottom=(600, 300))

# player
player_jump = pygame.image.load("graphics/player_jump.png").convert_alpha()
player_walk1 = pygame.image.load("graphics/player_walk_1.png").convert_alpha()
player_walk2 = pygame.image.load("graphics/player_walk_2.png").convert_alpha()
player_walk = [player_walk1, player_walk2]
player_index = 0
player_surface = player_walk[player_index]
player_rectangle = player_surface.get_rect(midbottom=(100, 300))
player_gravity = 0
sound_jump = pygame.mixer.Sound("audio/jump2.mp3")  # stort S
sound_jump.set_volume(0.5)

# huvudloop
while True:

    # stänga fönstret
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()       # stoppar pygame
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.pos)
                if player_rectangle.collidepoint(event.pos):
                    player_gravity = -20
                    sound_jump.play()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    # print("space nedtryckt")
                    player_gravity = -20
                    sound_jump.play()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    sound_bg.play(loops = -1)   # startar bg vid omstart
                    snail_rectangle.left = 800
                    start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(bg_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        display_score()

        # snail
        snail_index += 0.2
        snail_surface = snail_move[int(snail_index)%len(snail_move)]
        screen.blit(snail_surface, snail_rectangle)
        snail_rectangle.x -= 4
        if snail_rectangle.right < 0:
            snail_rectangle.left = 800

        # player
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom > 300:       # om spelaren är under marken
            player_rectangle.bottom = 300       # flytta upp på marken

        # vilken bild ska laddas in?
        if player_rectangle.bottom < 300:
            player_surface = player_jump
        else:
            player_index += 0.07
            player_surface = player_walk[int(player_index)%len(player_walk)]
        screen.blit(player_surface, player_rectangle)



        # Kollisioner
        if player_rectangle.colliderect(snail_rectangle):
            game_active = False
            sound_bg.stop()     # stoppar bakgrundsljudet
    else:
        screen.fill("Yellow")

    pygame.display.update()
    clock.tick(60)
