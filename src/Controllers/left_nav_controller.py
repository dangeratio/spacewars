# left_nav_controller.py
# description: this is the controller for the left nav inside the main gameplay screen
#
# ApplicationController
#     IntroController
#     MainController
#         LeftNavController*
#         MainNavController
#         MapNavController

from Tkinter import Frame
from Views.left_nav_view import *

# temp
from Views.popup_view import *


class LeftNavController(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.view = LeftNavView(self, self.parent.view)
        self.app = self.parent.app
        self.enabled = False

    def message(self, message):

        if message == 'enable':
            self.enabled = True
        elif message == 'disable':
            self.enabled = False
        elif message == 'new game':
            self.enabled = True
            self.view.build()
        else:
            if self.enabled:
                if message == 'refresh':
                    self.view.redraw()

    def button_next_planet_clicked(self, event):

        self.app.debug("Next Planet Clicked")
        popup = Popup('', 'text', 'button')
        popup.display(self.app.main_controller.view)

    def button_next_ship_clicked(self, event):
        self.app.debug("Next Ship Clicked")

    def button_home_planet_clicked(self, event):

        # global player, active_view
        conf = self.app.conf
        player = self.app.game.player

        self.app.debug("Home Planet Clicked")

        '''
        for planet in player.planets:
            if player.home_planet_name == planet.name:
                player.selected_planet = planet
                if active_view == "intro":
                    draw_intro_nav()
                elif active_view == "main":
                    build_main_nav()
        '''


    def button_end_turn_clicked(self, event):
        self.app.debug("End Turn Clicked")


