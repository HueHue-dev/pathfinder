import pygame as pg
from .cell import Cell


class Board:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.gap = width // rows
        self.color = (255, 255, 255)
        self.grid = []
        self.has_start_position = False
        self.has_target_position = False
        self.set_grid()

    def set_grid(self):
        for x in range(self.rows):
            self.grid.append([])
            for y in range(self.rows):
                cell = Cell(x, y, self.gap)
                self.grid[x].append(cell)

    def get_pos(self, pos):
        y, x = pos
        row = y // self.gap
        col = x // self.gap

        return row, col

    def draw_grid(self, win):
        for i in range(self.rows):
            pg.draw.line(win, self.color, (0, i * self.gap), (self.width, i * self.gap))
            for j in range(self.rows):
                pg.draw.line(win, self.color, (j * self.gap, 0), (j * self.gap, self.width))

    def draw(self, win):
        for row in self.grid:
            for cell in row:
                cell.draw(win)
        self.draw_grid(win)

