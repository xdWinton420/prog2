import pygame


pygame.init()

screen = pygame.display.set_mode((700, 400))
pygame.display.set_caption("PookMan")
clock = pygame.time.Clock()

bg_surface = pygame.image.load("graphics/Scene1 (1).png")
bg_surface2 = pygame.image.load("graphics/pixil-frame-0 (1).png")
bg_surface3 = pygame.image.load("graphics/Scene1 (2).png")
bg_surface4 = pygame.image.load("graphics/Scene2 (1).png")
bg_fight_surface = pygame.image.load("graphics/fight_emot_karl.png")
bg_fight_options = pygame.image.load("graphics/fight_options.png")
start_screen = pygame.image.load("graphics/första_scene.png")


playerx = 350
playery = 200

player_index = 0
player_surface = pygame.image.load("graphics/down_idle.png")
player_surface_right = pygame.image.load("graphics/right_idle.png")
player_surface_left = pygame.image.load("graphics/left_idle.png")
player_surface_up = pygame.image.load("graphics/up_idle.png")
player_rectangle = player_surface.get_rect(midbottom=(playerx, playery))
player_surface = pygame.transform.scale(player_surface, (20, 20))
player_surface_right = pygame.transform.scale(player_surface_right, (20, 20))
player_surface_left = pygame.transform.scale(player_surface_left, (20, 20))
player_surface_up = pygame.transform.scale(player_surface_up, (20, 20))
move = 0
room = 0
walk_count = 0
open_world = False
fight_world = False
first_scene = True
fight_option = 0
karl_health = 100
enemy_count = 0
player_health = 100

def direction():
    if move == 0:
        screen.blit(player_surface, player_rectangle)
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
    if first_scene:
        screen.blit(start_screen, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = pygame.mouse.get_pos()[0]
            posy = pygame.mouse.get_pos()[1]
            if posx > 259 and posx < 462 and posy > 17 and posy < 134:
                first_scene = False
                open_world = True
    if fight_world and enemy_count == 0:
        screen.blit(bg_fight_surface, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = pygame.mouse.get_pos()[0]
            posy = pygame.mouse.get_pos()[1]
            print(posx, posy)
            if posx > 506 and posy > 250:
                walk_count = 0
                fight_world = False
                open_world = True
            if posx > 250 and posx < 450 and posy > 323:
                fight_world = False
                fight_option = 1
    if fight_option == 1:
        screen.blit(bg_fight_options, (0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = pygame.mouse.get_pos()[0]
            posy = pygame.mouse.get_pos()[1]
            print(posx, posy)
            if posx < 307 and posy > 275 and posy < 377:
                print("You fkn idiot!")
                karl_health = 0
        if karl_health == 0:
            walk_count = 0
            fight_option = 0
            fight_world = False
            open_world = True
    if open_world:
        if room == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = pygame.mouse.get_pos()[0]
                posy = pygame.mouse.get_pos()[1]
                print(posx, posy)
            if player_rectangle.x > 430 and player_rectangle.y > 235:
                player_rectangle.x = 430
            if player_rectangle.y > 210 and player_rectangle.x > 440:
                player_rectangle.y = 210
            if player_rectangle.x < 248:
                player_rectangle.x = 248
            if player_rectangle.y < 155 and player_rectangle.x > 500:
                player_rectangle.y = 155
            if player_rectangle.x > 490 and player_rectangle.y < 155:
                player_rectangle.x = 490

            screen.blit(bg_surface, (0, 0))
            direction()
            if player_rectangle.x >= 670 and player_rectangle.y < 200 and player_rectangle.y > 100:
                player_rectangle.x = 5
                room = 1
            if player_rectangle.x > 300 and player_rectangle.x < 360 and player_rectangle.y >= 350:
                player_rectangle.y = 0
                room = 2
        elif room == 1:
            screen.blit(bg_surface4, (0, 0))
            direction()
            if player_rectangle.x <= 0 and player_rectangle.y < 200 and player_rectangle.y > 100:
                player_rectangle.x = 669
                room = 0
        elif room == 2:
            screen.blit(bg_surface3, (0, 0))
            direction()
            if player_rectangle.x > 300 and player_rectangle.x < 360 and player_rectangle.y <= 0:
                player_rectangle.y = 349
                room = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_rectangle.x -= 3
            move = 3
            walk_count += 5
        if player_rectangle.x < -3 : player_rectangle.x = -3
        if keys[pygame.K_d]:
            player_rectangle.x += 3
            move = 2
            walk_count += 5
        if player_rectangle.right > 700 : player_rectangle.right = 700
        if keys[pygame.K_w]:
            move = 1
            player_rectangle.y -= 3
            walk_count += 5
        if player_rectangle.y < 0 : player_rectangle.y = 0
        if keys[pygame.K_s]:
            move = 0
            player_rectangle.y += 3
            walk_count += 5
        if player_rectangle.bottom > 395 : player_rectangle.bottom = 395
        if walk_count > 3000:
            open_world = False
            fight_world = True



    pygame.display.update()
    clock.tick(60)
