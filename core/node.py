import pygame as pg
from .config import Config


class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.color = Config.COLOR_DEFAULT
        self.is_start = False
        self.is_barrier = False
        self.is_target = False
        self.neighbors = []
        self.previous = None
        self.f = 0
        self.g = 0
        self.h = 0

    def draw(self, win, show_values, font):
        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))
        if show_values:
            f_text = font.render('f: ' + str(self.f), True, Config.COLOR_TEXT)
            win.blit(f_text, (self.x + 10, self.y + 10))
            g_text = font.render('g: ' + str(self.g), True, Config.COLOR_TEXT)
            win.blit(g_text, (self.x + 50, self.y + 10))
            h_text = font.render('h: ' + str(self.h), True, Config.COLOR_TEXT)
            win.blit(h_text, (self.x + (self.width / 2) - 15, self.y + 40))

    def set_start(self):
        self.color = Config.COLOR_START
        self.is_start = True

    def set_target(self):
        self.color = Config.COLOR_TARGET
        self.is_target = True

    def set_barrier(self):
        self.color = Config.COLOR_BARRIER
        self.is_barrier = True

    def set_default(self):
        self.color = Config.COLOR_DEFAULT

    def set_path(self):
        self.color = Config.COLOR_PATH

    def set_closed(self):
        self.color = Config.COLOR_CLOSED

    def set_open(self):
        self.color = Config.COLOR_OPEN

    def __lt__(self, other):
        return False
