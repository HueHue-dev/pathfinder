import pygame as pg
from .node import Node
from .path import Path


class Board:
    def __init__(self, rows):
        self.rows = rows
        self.width = 800
        self.gap = self.width // rows
        self.color = (255, 255, 255)
        self.grid = []
        self.start_node = None
        self.target_node = None
        self.__set_grid()

    def __set_grid(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                node = Node(i, j, self.gap)
                self.grid[i].append(node)

    def set_neighbours(self, with_diagonal: bool):
        for row in self.grid:
            for node in row:
                if node.row < (self.rows - 1) and not self.grid[node.row + 1][node.col].is_barrier:  # Down
                    node.neighbors.append(self.grid[node.row + 1][node.col])
                if node.row > 0 and not self.grid[node.row - 1][node.col].is_barrier:  # Up
                    node.neighbors.append(self.grid[node.row - 1][node.col])
                if node.col < (self.rows - 1) and not self.grid[node.row][node.col + 1].is_barrier:  # Right
                    node.neighbors.append(self.grid[node.row][node.col + 1])
                if node.col > 0 and not self.grid[node.row][node.col - 1].is_barrier:  # Left
                    node.neighbors.append(self.grid[node.row][node.col - 1])
                if not with_diagonal:
                    continue
                if node.row < (self.rows - 1) and node.col < (self.rows - 1) and not self.grid[node.row + 1][node.col + 1].is_barrier:  # Down right
                    node.neighbors.append(self.grid[node.row + 1][node.col + 1])
                if node.row < (self.rows - 1) and node.col > 0 and not self.grid[node.row + 1][node.col - 1].is_barrier:  # Down left
                    node.neighbors.append(self.grid[node.row + 1][node.col - 1])
                if node.row > 0 and node.col < (self.rows - 1) and not self.grid[node.row - 1][node.col + 1].is_barrier:  # Up right
                    node.neighbors.append(self.grid[node.row - 1][node.col + 1])
                if node.row > 0 and node.col > 0 and not self.grid[node.row - 1][node.col - 1].is_barrier:  # Up left
                    node.neighbors.append(self.grid[node.row - 1][node.col - 1])

    def get_pos(self, pos):
        y, x = pos
        row = y // self.gap
        col = x // self.gap

        return row, col

    def has_start(self):
        return self.start_node is not None

    def has_target(self):
        return self.target_node is not None

    def draw_grid(self, win):
        for i in range(self.rows):
            if i < 1:
                continue
            pg.draw.line(win, self.color, (0, i * self.gap), (self.width, i * self.gap))
            for j in range(self.rows):
                if j < 1:
                    continue
                pg.draw.line(win, self.color, (j * self.gap, 0), (j * self.gap, self.width))

    def draw(self, win):
        for row in self.grid:
            for node in row:
                node.draw(win)
        self.draw_grid(win)

    def draw_path(self, win, path: Path):
        for node in path.get_path():
            if node.is_start or node.is_barrier or node.is_target:
                continue
            self.grid[node.row][node.col].set_path()
            self.draw(win)

    def draw_open_list(self, win, open_list):
        for node in open_list:
            if node.is_start or node.is_barrier or node.is_target:
                continue
            self.grid[node.row][node.col].set_closed()
            self.draw(win)

    def reset(self):
        self.grid = []
        self.start_node = None
        self.target_node = None
        self.__set_grid()
