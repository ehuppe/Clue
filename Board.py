import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Welcome to Clue!")
screen.fill((255, 248, 220))

run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    pygame.display.update()

pygame.quit()
