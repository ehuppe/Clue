
import pygame
import Constants

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))
    return screen

def game_loop(surface, gameMap):
    run = True
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw_map(surface, gameMap)
        draw_grid(surface)
        pygame.display.update()
    pygame.quit()

def get_tile_color(tile_contents):
    tile_color = Constants.BLACK
    if (tile_contents == "-"):
        tile_color = Constants.CREAM
    if (tile_contents == "k"):
        tile_color = Constants.KITCHEN
    if (tile_contents == "b"):
        tile_color = Constants.BALLROOM
    if (tile_contents == "c"):
        tile_color = Constants.CONSERV
    if (tile_contents == "d"):
        tile_color = Constants.DINING
    if (tile_contents == "l"):
        tile_color = Constants.LOUNGE
    if (tile_contents == "s"):
        tile_color = Constants.STUDY
    return tile_color

def draw_map(surface, map_tiles):
    for j, tile in enumerate(map_tiles):
        for i, tile_contents in tile:
            myrect = pygame.Rect(i * Constants.BLOCK_WIDTH, j * Constants.BLOCK_HEIGHT, Constants.BLOCK_WIDTH, Constants.BLOCK_HEIGHT)
            pygame.draw.rect(surface, get_tile_color(tile_contents), myrect)

def draw_grid(surface):
    for i in range(Constants.BLOCKS_WIDE):
        new_height = i * Constants.BLOCK_HEIGHT
        new_width = i * Constants.BLOCK_WIDTH
        pygame.draw.line(surface, Constants.BLACK, (0, new_height), (Constants.SCREEN_WIDTH, new_height), 2)
        pygame.draw.line(surface, Constants.BLACK, (new_width, 0), (new_width, Constants.SCREEN_HEIGHT), 2)

def read_map(mapfile):
    with open(mapfile, 'r') as f:
        gameMap = f.readlines()
    gameMap = [line.strip() for line in gameMap]  # for every line, strip new line character
    return (gameMap)

def main():
    gameMap = read_map(Constants.MAPFILE)
    surface = initialize_game()
    game_loop(surface, gameMap)
