import pygame as pg
import pygame_gui as pgui
from typing import Optional
from .board import Board
from .astar import AStar
from .heuristicFactory import HeuristicFactory
from .config import Config
from .path import Path


class App:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Config.WIDTH, Config.HEIGHT))
        pg.display.set_caption(Config.APP_TITLE)
        self.clock = pg.time.Clock()
        self.manager = pgui.UIManager((Config.WIDTH, Config.HEIGHT))
        
        self.board = Board(Config.ROWS)
        self.a_star = AStar()
        self.path: Optional[Path] = None
        self.is_show_values = False
        
        self._setup_ui()

    def _setup_ui(self):
        self.search_btn = pgui.elements.UIButton(
            relative_rect=pg.Rect((690, Config.HEIGHT - 60), (100, 50)),
            text='Search', manager=self.manager
        )
        self.search_btn.disable()

        self.reset_btn = pgui.elements.UIButton(
            relative_rect=pg.Rect((690, Config.HEIGHT - 140), (100, 50)),
            text='Reset', manager=self.manager
        )

        self.exit_btn = pgui.elements.UIButton(
            relative_rect=pg.Rect((10, Config.HEIGHT - 60), (100, 50)),
            text='Exit', manager=self.manager
        )

        self.heuristic_menu = pgui.elements.UIDropDownMenu(
            options_list=list(HeuristicFactory.heuristics.keys()),
            starting_option=HeuristicFactory.get_default(),
            relative_rect=pg.Rect((480, Config.HEIGHT - 140), (200, 50)),
            manager=self.manager
        )

        self.show_values_btn = pgui.elements.UIButton(
            relative_rect=pg.Rect((10, Config.HEIGHT - 140), (150, 50)),
            text='Show Values', manager=self.manager
        )
        self.show_values_btn.disable()

    def run(self):
        while True:
            time_delta = self.clock.tick(60) / 1000.0
            
            for event in pg.event.get():
                self.manager.process_events(event)
                self._handle_event(event)

            self.manager.update(time_delta)
            self._draw()

    def _draw(self):
        self.screen.fill(Config.COLOR_DEFAULT)
        self.board.draw(
            self.screen, 
            self.is_show_values, 
            self.a_star.get_open_list(), 
            self.a_star.get_closed_list(), 
            self.path
        )
        self.manager.draw_ui(self.screen)
        pg.display.update()

    def _handle_event(self, event):
        if event.type == pg.QUIT:
            self._exit_app()
        
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
        if any(p >= self.board.width for p in pos):
            return
            
        row, col = self.board.get_pos(pos)
        node = self.board.grid[row][col]
        
        if event.button == 1:  # Left click
            if not self.board.has_start():
                self.board.set_start_node(node)
            elif not self.board.has_target():
                self.board.set_target_node(node)
                self.search_btn.enable()
        elif event.button == 3:  # Right click
            self.board.set_barrier(node)

    def _handle_ui_button_click(self, event):
        if event.ui_element == self.search_btn:
            self._start_search()

        elif event.ui_element == self.show_values_btn:
            self.is_show_values = not self.is_show_values

        elif event.ui_element == self.reset_btn:
            self._reset_app()

        elif event.ui_element == self.exit_btn:
            self._exit_app()

    def _start_search(self):
        self.board.set_neighbours(self.a_star.get_heuristic().is_diagonal())
        self.path = self.a_star.search(self.board)
        if self.path:
            self.show_values_btn.enable()

    def _reset_app(self):
        self.board.reset()
        self.a_star.reset()
        self.path = None
        self.search_btn.disable()
        self.show_values_btn.disable()

    def _exit_app(self):
        pg.quit()
        raise SystemExit
