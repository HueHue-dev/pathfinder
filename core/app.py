import pygame as pg
from .board import Board
from .astar import AStar


class App:
    def __init__(self):
        pg.init()
        self.width = 800
        self.screen = pg.display.set_mode((self.width, self.width))
        self.clock = pg.time.Clock()

    def run(self):
        board = Board(10, self.width)
        a_star = AStar()

        while True:
            board.draw(self.screen)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit

                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pg.mouse.get_pos()
                    row, col = board.get_pos(pos)
                    cell = board.grid[row][col]
                    if board.start_cell is None:
                        cell.set_start()
                        board.start_cell = cell
                    elif board.target_cell is None:
                        cell.set_target()
                        board.target_cell = cell
                    elif board.has_start() and board.has_target():
                        cell.set_barrier()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        board.set_neighbours()
                        path = a_star.search(board)
                        board.draw_path(self.screen, path)
                        pg.display.update()
                        board.draw_open_list(self.screen, a_star.get_open_list())
                        pg.display.update()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        board.reset()
                        a_star.reset()
