# main_controller.py
# description: this is the controller for the main gameplay screen, containing left nav, main nav, and map nap
#
# ApplicationController
#     IntroController
#     MainController*
#         LeftNavController
#         MainNavController
#         MapNavController

# from Tkinter import Frame
from Controllers.main_nav_controller import *
from Controllers.left_nav_controller import *
from Controllers.map_nav_controller import *
from Controllers.intro_controller import *
from Views.main_view import *


class MainController(Frame):
    def __init__(self, parent):

        self.parent = parent
        self.app = self.parent

        # define view
        self.view = MainView(self)
        self.enabled = True

        # build sub-controller objects
        self.app.debug("Building Controller Objects")
        self.intro_controller = IntroController(self)
        self.left_nav_controller = LeftNavController(self)
        self.main_nav_controller = MainNavController(self)
        self.map_nav_controller = MapNavController(self)

        # trigger display of intro view
        self.app.debug_messaging("MessageSend: display intro")
        self.intro_controller.message("display intro")

    def broadcast(self, message):

        if message == 'refresh':        # attempt refresh, if first cycle, they will not exist
            try:
                self.intro_controller.message(message)
            except AttributeError:
                pass
            else:
                pass

            try:
                self.left_nav_controller.message(message)
            except AttributeError:
                pass
            else:
                pass

            try:
                self.main_nav_controller.message(message)
            except AttributeError:
                pass
            else:
                pass

            try:
                self.map_nav_controller.message(message)
            except AttributeError:
                pass
            else:
                pass
        else:
            self.intro_controller.message(message)
            self.left_nav_controller.message(message)
            self.main_nav_controller.message(message)
            self.map_nav_controller.message(message)

    def message(self, message):

        if message == 'new game':
            self.app.new_game()
            self.left_nav_controller.message(message)
            self.main_nav_controller.message(message)
            self.map_nav_controller.message(message)

    def remove_this(self):
        self.view.destroy()

'''
    def trigger_display(self, view):

        if view == 'intro':
            # self.intro_screen = IntroScreen(self.controller.main_controller.intro_controller, self)
            self.intro_controller.incoming("displayintro")
        elif view == 'main':
            # create nav's for the main view
            self.main_nav = MainNavView()
            self.left_nav = LeftNavView()
            # self.map_nav = MapNav()       # not yet implemented
'''
