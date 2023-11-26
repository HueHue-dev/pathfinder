import pygame as pg
from .cell import Cell


class Board:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.gap = width // rows
        self.color = (255, 255, 255)
        self.grid = []
        self.start_cell = None
        self.target_cell = None
        self.set_grid()

    def set_grid(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                cell = Cell(i, j, self.gap)
                self.grid[i].append(cell)

    def get_pos(self, pos):
        y, x = pos
        row = y // self.gap
        col = x // self.gap

        return row, col

    def has_start(self):
        return self.start_cell is not None

    def has_target(self):
        return self.target_cell is not None

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

