# main_nav_controller.py
# description: this is the main nav controller, controlling the "planet view" in the main gameplay screen,
#              the section with all the planets displayed inside of it
#
# ApplicationController
#     IntroController
#     MainController
#         LeftNavController
#         MainNavController*
#         MapNavController

from Tkinter import Frame
from Views.main_nav_view import *


class MainNavController(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.app = self.parent.app
        self.view = MainNavView(self, self.parent.view)

    def select_planet(self, event, planet):

        global main_window

        # w = event.widget
        self.app.player.selected_planet = planet
        self.app.debug(("SelectingPlanet:", planet.name))

        main_window.refresh()

    def message(self, message):
        if message == 'new game':
            self.view.build()

