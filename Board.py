import pygame
import Constants

pygame.init()
screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
pygame.display.set_caption("Welcome to Clue!")

for j in range(2, 7):
    for i in range(0, 12):
        tile = pygame.Rect((Constants.BLOCK_WIDTH * i), (Constants.BLOCK_HEIGHT * j), Constants.BLOCK_WIDTH, Constants.BLOCK_HEIGHT)
        pygame.draw.rect(screen, Constants.CREAM, tile)

kitchenTile = pygame.Rect(0, 0, (Constants.BLOCK_WIDTH * 4), (Constants.BLOCK_HEIGHT * 2))
pygame.draw.rect(screen, Constants.KITCHEN, kitchenTile)

ballroomTile = pygame.Rect((Constants.BLOCK_WIDTH * 4), 0, (Constants.BLOCK_WIDTH * 4), (Constants.BLOCK_HEIGHT * 2))
pygame.draw.rect(screen, Constants.BALLROOM, ballroomTile)

conservTile = pygame.Rect((Constants.BLOCK_WIDTH * 8), 0, (Constants.BLOCK_WIDTH * 4), (Constants.BLOCK_HEIGHT * 2))
pygame.draw.rect(screen, Constants.CONSERV, conservTile)

diningTile = pygame.Rect(0, (Constants.SCREEN_HEIGHT - (Constants.BLOCK_HEIGHT * 2)), (Constants.BLOCK_WIDTH * 4), (Constants.BLOCK_HEIGHT * 2))
pygame.draw.rect(screen, Constants.DINING, diningTile)

loungeTile = pygame.Rect((Constants.BLOCK_WIDTH * 4), (Constants.SCREEN_HEIGHT - (Constants.BLOCK_HEIGHT * 2)),(Constants.BLOCK_WIDTH * 4), (Constants.BLOCK_HEIGHT * 2))
pygame.draw.rect(screen, Constants.LOUNGE, loungeTile)

studyTile = pygame.Rect((Constants.BLOCK_WIDTH * 8), (Constants.SCREEN_HEIGHT - (Constants.BLOCK_HEIGHT * 2)), (Constants.BLOCK_WIDTH * 4), (Constants.BLOCK_HEIGHT * 2))
pygame.draw.rect(screen, Constants.STUDY, studyTile)

#for j in range(1, 12):
    #pygame.draw.line(screen, Constants.BLACK, (Constants.BLOCK_WIDTH * j), (Constants.BLOCK_HEIGHT * 5))

run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    pygame.display.update()
pygame.quit()
