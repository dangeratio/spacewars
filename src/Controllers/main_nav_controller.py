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


class MainNavController(Frame):
    def __init__(self):
        pass

    def select_planet(event, planet):

        global main_window

        # w = event.widget
        player.selected_planet = planet
        if conf.debug == 1:
            print "SelectingPlanet:", planet.name
        main_window.refresh()

