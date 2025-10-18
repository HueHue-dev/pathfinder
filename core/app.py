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
        is_show_values = False

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
        heuristic = pgui.elements.UIDropDownMenu(
            options_list=HeuristicFactory.heuristics.keys(),
            starting_option=HeuristicFactory.get_default(),
            relative_rect=pg.Rect((480, self.height - 140), (200, 50)),
            manager=self.manager
        )
        show_values = pgui.elements.UIButton(
            relative_rect=pg.Rect((10, self.height - 140), (150, 50)),
            text='Show Values',
            manager=self.manager
        )
        show_values.disable()

        while True:
            board.draw(self.screen, is_show_values)
            pg.display.update()
            for event in pg.event.get():
                self.manager.process_events(event)
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    row, col = board.get_pos(pos)
                    if pos[1] >= board.width:
                        continue
                    node = board.grid[row][col]
                    if event.button == 1:
                        if board.start_node is None:
                            node.set_start()
                            board.start_node = node
                        elif board.target_node is None:
                            node.set_target()
                            board.target_node = node
                            search.enable()

                    if event.button == 3:
                        node.set_barrier()

                if event.type == pgui.UI_BUTTON_PRESSED:
                    if event.ui_element == search:
                        board.set_neighbours(a_star.get_heuristic().is_diagonal())
                        path = a_star.search(board)
                        board.draw_path(path)
                        board.draw_open_list(a_star.get_open_list())
                        board.draw_closed_list(a_star.get_closed_list(), path)
                        show_values.enable()

                    if event.ui_element == show_values:
                        is_show_values = not is_show_values

                    if event.ui_element == reset:
                        board.reset()
                        a_star.reset()

                    if event.ui_element == end:
                        pg.quit()
                        raise SystemExit

                if event.type == pgui.UI_DROP_DOWN_MENU_CHANGED:
                    if event.ui_element == heuristic:
                        a_star.set_heuristic(event.text)
                        board.set_neighbours(a_star.get_heuristic().is_diagonal())

            self.manager.update(self.time_delta)
            self.manager.draw_ui(self.screen)
            pg.display.update()
