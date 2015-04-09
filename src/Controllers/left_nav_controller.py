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


class LeftNavController(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.view = LeftNavView(self, self.parent.view)
        self.enabled = False

    def message(self, message):

        if message == 'enable':
            self.enabled = True
        elif message == 'disable':
            self.enabled = True
        else:
            if self.enabled:
                if message == 'refresh':
                    self.view.redraw()

    def build(self):        # prev: build_left_nav_menu

        global left_nav, left_canvas, left

        left_nav.place(x=0, y=0)

        left = LeftNav(main_window, player, left_nav)

    def button_next_planet_clicked(self, event):
        if conf.debug == 1:
            print "Next Planet Clicked"
        popup = Popup('', 'text', 'button')
        frame_obj = event.widget.master.master.master.master

        popup.display(frame_obj)

    def button_next_ship_clicked(self, event):
        if conf.debug == 1:
            print "Next Ship Clicked"
        pass


    def button_home_planet_clicked(self, event):

        global player, active_view

        if conf.debug == 1:
            print "Home Planet Clicked"
        for planet in player.planets:
            if player.home_planet_name == planet.name:
                player.selected_planet = planet
                if active_view == "intro":
                    draw_intro_nav()
                elif active_view == "main":
                    build_main_nav()
        pass


    def button_end_turn_clicked(self, event):
        if conf.debug == 1:
            print "End Turn Clicked"
        pass


