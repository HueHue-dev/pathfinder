import pygame as pg


class Cell:
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
        self.g = 0

    def draw(self, win):
        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

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

    def is_barrier(self):
        return self.is_barrier

    def set_path(self):
        self.color = (0, 89, 255)

    def update_neighbors(self, board):
        if self.row < (board.rows - 1) and not board.grid[self.row + 1][self.col].is_barrier:  # Down
            self.neighbors.append(board.grid[self.row + 1][self.col])
        if self.row > 0 and not board.grid[self.row - 1][self.col].is_barrier:  # Up
            self.neighbors.append(board.grid[self.row - 1][self.col])
        if self.col < board.rows - 1 and not board.grid[self.row][self.col + 1].is_barrier:  # Right
            self.neighbors.append(board.grid[self.row][self.col + 1])
        if self.col > 0 and not board.grid[self.row][self.col - 1].is_barrier:  # Left
            self.neighbors.append(board.grid[self.row][self.col - 1])
