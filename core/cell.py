import pygame as pg


class Cell:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.col = col
        self.width = width
        self.color = (0, 0, 0)

    def draw(self, win):
        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def set_start(self):
        self.color = (0, 128, 34)

    def set_target(self):
        self.color = (155, 0, 0)

    def set_barrier(self):
        self.color = (255, 255, 255)

    def set_default(self):
        self.color = (0, 0, 0)