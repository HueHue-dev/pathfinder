import pygame as pg


class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.color = (0, 0, 0)
        self.is_start = False
        self.is_barrier = False
        self.is_target = False
        self.neighbors = []
        self.previous = None,
        self.f = 0
        self.g = 0
        self.h = 0
        self.__font = pg.font.SysFont(None, 17)

    def draw(self, win, show_values):
        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        if show_values:
            f_text = self.__font.render('f: ' + str(self.f), True, (255, 255, 255))
            win.blit(f_text, (self.x + 10, self.y + 10))
            g_text = self.__font.render('g: ' + str(self.g), True, (255, 255, 255))
            win.blit(g_text, (self.x + 50, self.y + 10))
            h_text = self.__font.render('h: ' + str(self.h), True, (255, 255, 255))
            win.blit(h_text, (self.x + (self.width / 2) - 15, self.y + 40))

    def set_start(self):
        self.color = (0, 128, 34)
        self.is_start = True

    def set_target(self):
        self.color = (155, 0, 0)
        self.is_target = True

    def set_barrier(self):
        self.color = (255, 255, 255)
        self.is_barrier = True

    def set_default(self):
        self.color = (0, 0, 0)

    def set_path(self):
        self.color = (0, 89, 255)

    def set_closed(self):
        self.color = (100, 100, 100)

    def set_open(self):
        self.color = (152, 179, 0)
