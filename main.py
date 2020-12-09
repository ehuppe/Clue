import pygame

 # initialize the pygame
pygame.init()

 # create the screen
screen = pygame.display.set_mode((1000,1000))

pygame.display.set_caption("Welcome to Clue!")

x = 10
y = 10
vel = 5

run = True
while (run):
    pygame.time.delay(100)

    # check for events from user -- moving mouse, etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y += vel
    if keys[pygame.K_DOWN]:
        y -= vel

    #screen.fill(0,0,0)
    pygame.draw.circle(screen, (255,48,48), (x, y), 20)
    pygame.draw.line(screen, (248,248,255), (50,0), (50,1000), 10)
    pygame.display.update()

pygame.quit()

