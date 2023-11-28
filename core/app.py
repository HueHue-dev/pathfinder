import pygame as pg
import pygame_gui as pgui
from .board import Board
from .astar import AStar
from .heuristicFactory import HeuristicFactory


class App:
    def __init__(self):
        pg.init()
        self.width = 800
        self.height = 960
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.time_delta = self.clock.tick(60)
        self.manager = pgui.UIManager((self.width, self.height))

    def run(self):
        board = Board(10)
        a_star = AStar()

        search = pgui.elements.UIButton(
            relative_rect=pg.Rect((690, self.height - 60), (100, 50)),
            text='Search',
            manager=self.manager
        )
        search.disable()
        reset = pgui.elements.UIButton(
            relative_rect=pg.Rect((690, self.height - 140), (100, 50)),
            text='Reset',
            manager=self.manager
        )
        end = pgui.elements.UIButton(
            relative_rect=pg.Rect((10, self.height - 60), (100, 50)),
            text='Exit',
            manager=self.manager
        )
        dropdown = pgui.elements.UIDropDownMenu(
            options_list=HeuristicFactory.heuristics.keys(),
            starting_option=HeuristicFactory.get_default(),
            relative_rect=pg.Rect((480, self.height - 140), (200, 50)),
            manager=self.manager
        )

        while True:
            board.draw(self.screen)
            pg.display.update()
            for event in pg.event.get():
                self.manager.process_events(event)

                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pg.mouse.get_pos()
                    row, col = board.get_pos(pos)
                    if pos[1] >= board.width:
                        continue
                    node = board.grid[row][col]
                    if board.start_node is None:
                        node.set_start()
                        board.start_node = node
                    elif board.target_node is None:
                        node.set_target()
                        board.target_node = node
                        search.enable()
                    elif board.has_start() and board.has_target():
                        node.set_barrier()

                if event.type == pgui.UI_BUTTON_PRESSED:
                    if event.ui_element == search:
                        board.set_neighbours(a_star.get_heuristic().is_diagonal())
                        path = a_star.search(board)
                        board.draw_path(self.screen, path)
                        board.draw_open_list(self.screen, a_star.get_open_list())
                        board.draw_closed_list(self.screen, a_star.get_closed_list(), path)

                    if event.ui_element == reset:
                        board.reset()
                        a_star.reset()

                    if event.ui_element == end:
                        pg.quit()
                        raise SystemExit

                if event.type == pgui.UI_DROP_DOWN_MENU_CHANGED:
                    a_star.set_heuristic(event.text)
                    board.set_neighbours(a_star.get_heuristic().is_diagonal())

            self.manager.update(self.time_delta)
            self.manager.draw_ui(self.screen)
            pg.display.update()
