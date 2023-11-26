import pygame as pg
from .cell import Cell
from .path import Path


class Board:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.gap = width // rows
        self.color = (255, 255, 255)
        self.grid = []
        self.start_cell = None
        self.target_cell = None
        self.__set_grid()

    def __set_grid(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                cell = Cell(i, j, self.gap)
                self.grid[i].append(cell)

    def set_neighbours(self):
        for row in self.grid:
            for cell in row:
                if cell.row < (self.rows - 1) and not self.grid[cell.row + 1][cell.col].is_barrier:  # Down
                    cell.neighbors.append(self.grid[cell.row + 1][cell.col])
                if cell.row > 0 and not self.grid[cell.row - 1][cell.col].is_barrier:  # Up
                    cell.neighbors.append(self.grid[cell.row - 1][cell.col])
                if cell.col < self.rows - 1 and not self.grid[cell.row][cell.col + 1].is_barrier:  # Right
                    cell.neighbors.append(self.grid[cell.row][cell.col + 1])
                if cell.col > 0 and not self.grid[cell.row][cell.col - 1].is_barrier:  # Left
                    cell.neighbors.append(self.grid[cell.row][cell.col - 1])

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

    def draw_path(self, win, path: Path):
        for cell in path.get_path():
            if cell.is_start or cell.is_barrier or cell.is_target:
                continue
            self.grid[cell.row][cell.col].set_path()
            self.draw(win)

