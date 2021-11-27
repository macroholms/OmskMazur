import sys

import pygame

def draw_crest(screen):
    pygame.draw.polygon(screen, pygame.Color("red"), [(1, 1), (int(width) - 1, 1),
                                                        (int(width) - 1, int(height) - 1), (1, int(height) - 1)])

if __name__ == '__main__':

    width, height = sys.stdin.read().split()
    a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    b = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    flag = False
    for i in width:
        if i in a or i in b:
            flag = True
    if "." in width or "." in height or flag is True:
        print("Неправильный формат ввода")
    else:
        pygame.init()
        size = int(width), int(height)
        screen = pygame.display.set_mode(size)
        draw_crest(screen)
        pygame.display.flip()
        pygame.display.set_caption("Крест")
        while pygame.event.wait().type != pygame.QUIT:
            pass
        pygame.quit()