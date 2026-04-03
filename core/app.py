import pygame as pg
import pygame_gui as pgui
from .board import Board
from .astar import AStar
from .heuristicFactory import HeuristicFactory
from .config import Config


class App:
    def __init__(self):
        pg.init()
        self.width = Config.WIDTH
        self.height = Config.HEIGHT
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.time_delta = self.clock.tick(60)
        self.manager = pgui.UIManager((self.width, self.height))
        
        self.board = Board(Config.ROWS)
        self.a_star = AStar()
        self.is_show_values = False
        self.__setup_ui()

    def __setup_ui(self):
        self.search_btn = pgui.elements.UIButton(
            relative_rect=pg.Rect((690, self.height - 60), (100, 50)),
            text='Search',
            manager=self.manager
        )
        self.search_btn.disable()
        self.reset_btn = pgui.elements.UIButton(
            relative_rect=pg.Rect((690, self.height - 140), (100, 50)),
            text='Reset',
            manager=self.manager
        )
        self.exit_btn = pgui.elements.UIButton(
            relative_rect=pg.Rect((10, self.height - 60), (100, 50)),
            text='Exit',
            manager=self.manager
        )
        self.heuristic_menu = pgui.elements.UIDropDownMenu(
            options_list=HeuristicFactory.heuristics.keys(),
            starting_option=HeuristicFactory.get_default(),
            relative_rect=pg.Rect((480, self.height - 140), (200, 50)),
            manager=self.manager
        )
        self.show_values_btn = pgui.elements.UIButton(
            relative_rect=pg.Rect((10, self.height - 140), (150, 50)),
            text='Show Values',
            manager=self.manager
        )
        self.show_values_btn.disable()

    def run(self):
        while True:
            self.board.draw(self.screen, self.is_show_values)
            pg.display.update()
            for event in pg.event.get():
                self.manager.process_events(event)
                self._handle_event(event)

            self.manager.update(self.time_delta)
            self.manager.draw_ui(self.screen)
            pg.display.update()

    def _handle_event(self, event):
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        
        if event.type == pg.MOUSEBUTTONDOWN:
            self._handle_mouse_click(event)

        if event.type == pgui.UI_BUTTON_PRESSED:
            self._handle_ui_button_click(event)

        if event.type == pgui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == self.heuristic_menu:
                self.a_star.set_heuristic(event.text)
                self.board.set_neighbours(self.a_star.get_heuristic().is_diagonal())

    def _handle_mouse_click(self, event):
        pos = pg.mouse.get_pos()
        if pos[1] >= self.board.width:
            return
            
        row, col = self.board.get_pos(pos)
        node = self.board.grid[row][col]
        
        if event.button == 1:  # Left click
            if self.board.start_node is None:
                node.set_start()
                self.board.start_node = node
            elif self.board.target_node is None:
                node.set_target()
                self.board.target_node = node
                self.search_btn.enable()
        elif event.button == 3:  # Right click
            node.set_barrier()

    def _handle_ui_button_click(self, event):
        if event.ui_element == self.search_btn:
            self.board.set_neighbours(self.a_star.get_heuristic().is_diagonal())
            path = self.a_star.search(self.board)
            if path:
                self.board.draw_path(path)
                self.board.draw_open_list(self.a_star.get_open_list())
                self.board.draw_closed_list(self.a_star.get_closed_list(), path)
                self.show_values_btn.enable()

        if event.ui_element == self.show_values_btn:
            self.is_show_values = not self.is_show_values

        if event.ui_element == self.reset_btn:
            self.board.reset()
            self.a_star.reset()
            self.search_btn.disable()
            self.show_values_btn.disable()

        if event.ui_element == self.exit_btn:
            pg.quit()
            raise SystemExit
