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


class MainNavController(object):
    def __init__(self, parent):
        self.parent = parent
        self.app = self.parent.app
        self.view = MainNavView(self, self.parent.view)

    def select_planet(self, event, planet):

        self.app.debug(("SelectingPlanet:", planet.name))

        # redraw old and new planets
        self.app.game.player.last_selected_planet = self.app.game.player.selected_planet
        self.app.game.player.selected_planet = planet
        self.view.redraw_planet(self.app.game.player.selected_planet)

        #refresh left nav
        self.parent.left_nav_controller.message('refresh')

    def message(self, message):
        if message == 'new game':
            self.view.build()



