import pygame

pygame.init()

screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("PookMan")
clock = pygame.time.Clock()

bg_surface = pygame.image.load("graphics/Scene1 (1).png")
bg_surface2 = pygame.image.load("graphics/pixil-frame-0 (1).png")

playerx = 350
playery = 200

player_index = 0
player_walk_0 = pygame.image.load("graphics/down_idle.png")
player_surface_right = pygame.image.load("graphics/right_idle.png")
player_surface_left = pygame.image.load("graphics/left_idle.png")
player_surface_up = pygame.image.load("graphics/up_idle.png")
player_walk_0 = pygame.transform.scale(player_walk_0, (20, 20))
player_surface_right = pygame.transform.scale(player_surface_right, (20, 20))
player_surface_left = pygame.transform.scale(player_surface_left, (20, 20))
player_surface_up = pygame.transform.scale(player_surface_up, (20, 20))
player_walk_1 = pygame.image.load("graphics/walk_down_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/walk_down_2.png").convert_alpha()
player_move = [player_walk_0, player_walk_1, player_walk_2]
snail_index = 0
player_surface_down = player_move[snail_index]
player_rectangle = player_surface_down.get_rect(midbottom=(playerx, playery))
move = 0
room = 0

def direction():
    if move == 0:
        screen.blit(player_surface_down, player_rectangle)
    if move == 1:
        screen.blit(player_surface_up, player_rectangle)
    if move == 2:
        screen.blit(player_surface_right, player_rectangle)
    if move == 3:
        screen.blit(player_surface_left, player_rectangle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    print(player_rectangle.x, player_rectangle.y)
    if room == 0:
        screen.blit(bg_surface, (0, 0))
        direction()
        if player_rectangle.x >= 670 and player_rectangle.y < 200 and player_rectangle.y > 100:
            player_rectangle.x = 0
            room = 1
        if player_rectangle.x > 300 and player_rectangle.x < 360 and player_rectangle.y >= 350:
            player_rectangle.y = 0
            room = 1
    elif room == 1:
        screen.blit(bg_surface2, (0, 0))
        direction()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rectangle.x -= 3
        move = 3
    if player_rectangle.x < -3 : player_rectangle.x = -3
    if keys[pygame.K_d]:
        player_rectangle.x += 3
        move = 2
    if player_rectangle.right > 700 : player_rectangle.right = 700
    if keys[pygame.K_w]:
        move = 1
        player_rectangle.y -= 3
    if player_rectangle.y < 0 : player_rectangle.y = 0
    if keys[pygame.K_s]:
        move = 0
        snail_index += 0.2
        snail_surface = player_move[int(snail_index) % len(player_move)]
        screen.blit(snail_surface, player_rectangle)
        player_rectangle.y += 3
    if player_rectangle.bottom > 395 : player_rectangle.bottom = 395

    pygame.display.update()
    clock.tick(60)
