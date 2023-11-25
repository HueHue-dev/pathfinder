import pygame as pg
from .board import Board


class App:
    def __init__(self):
        pg.init()
        self.width = 800
        self.screen = pg.display.set_mode((self.width, self.width))
        self.clock = pg.time.Clock()

    def run(self):
        board = Board(10, self.width)

        while True:
            board.draw(self.screen)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit
                if pg.mouse.get_pressed()[0]:
                    pos = pg.mouse.get_pos()
                    row, col = board.get_pos(pos)
                    cell = board.grid[row][col]
                    if not board.has_start_position:
                        cell.set_start()
                        board.has_start_position = True
                    elif not board.has_target_position:
                        cell.set_target()
                        board.has_target_position = True
                    elif board.has_start_position and board.has_target_position:
                        cell.set_barrier()
