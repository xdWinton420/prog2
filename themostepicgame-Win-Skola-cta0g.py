import pygame

pygame.init()

screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("PookMan")
clock = pygame.time.Clock()

bg_surface = pygame.image.load("graphics/pixilart-drawing.png")
bg_surface2 = pygame.image.load("graphics/pixil-frame-0 (1).png")

playerx = 350
playery = 200
player_surface = pygame.image.load("graphics/char_walk_right.gif").convert_alpha()
player_surface_scaled = pygame.transform.scale(player_surface, (50, 50))
player_rectangle = player_surface_scaled.get_rect(midbottom=(playerx, playery))

room = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    print(player_rectangle.x, player_rectangle.y)
    if room == 0:
        screen.blit(bg_surface, (0, 0))
        screen.blit(player_surface_scaled, player_rectangle)
        if player_rectangle.x > 300 and player_rectangle.x < 360 and player_rectangle.y <= 0:
            player_rectangle.y = 400
            room = 1
        if player_rectangle.x >= 670 and player_rectangle.y < 200 and player_rectangle.y > 100:
            player_rectangle.x = 0
            room = 1
    elif room == 1:
        screen.blit(bg_surface2, (0, 0))
        screen.blit(player_surface_scaled, player_rectangle)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rectangle.x -= 5
    if player_rectangle.x < -20 : player_rectangle.x = -20
    if keys[pygame.K_d]:
        player_rectangle.x += 5
    if player_rectangle.right > 720 : player_rectangle.right = 720
    if keys[pygame.K_w]:
        player_rectangle.y -= 5
    if player_rectangle.y < -20 : player_rectangle.y = -20
    if keys[pygame.K_s]:
        player_rectangle.y += 5
    if player_rectangle.bottom > 400 : player_rectangle.bottom = 400

    pygame.display.update()
    clock.tick(60)
