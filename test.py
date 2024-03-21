import sys
import pygame


bg_surface = pygame.image.load("graphics/pixilart-drawing.png")

def main():
    width, height = 640, 480
    hbox, vbox = 20, 20
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    rect = pygame.Rect(0, 0, hbox, vbox)
    velocity = (0, 0)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.blit(bg_surface, (0, 0))

        keys = pygame.key.get_pressed()

        # booster
        move = 8 if keys[pygame.K_LSHIFT] else 4

        if keys[pygame.K_a]:  #to move left
            rect.x -= move
        if rect.x < 0 : rect.x = 0

        if keys[pygame.K_d]: #to move right
            rect.x += move
        if rect.x > width-hbox : rect.x = width - hbox

        if keys[pygame.K_w]:  #to move up
            rect.y -= move
        if rect.y < 0: rect.y = 0

        if keys[pygame.K_s]: #to move down
            rect.y += move
        if rect.y > height - hbox: rect.y = height - vbox

        screen.fill((40, 40, 40))
        pygame.draw.rect(screen, (150, 200, 20), rect)

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
    sys.exit()