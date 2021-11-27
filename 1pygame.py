import sys

import pygame

width, height = sys.stdin.read().split()

def draw_crest(screen):
    pygame.draw.polygon(screen, pygame.Color("white"), [(0, 0), (int(width), int(height))], 5)
    pygame.draw.polygon(screen, pygame.Color("white"), [(int(width), 0), (0, int(height))], 5)

if __name__ == '__main__':
    pygame.init()
    size = int(width), int(height)
    screen = pygame.display.set_mode(size)
    draw_crest(screen)
    pygame.display.flip()
    pygame.display.set_caption("Крест")
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()