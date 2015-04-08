# main_controller.py
# description: this is the controller for the main gameplay screen, containing left nav, main nav, and map nap
#
# ApplicationController
#     IntroController
#     MainController*
#         LeftNavController
#         MainNavController
#         MapNavController

from Tkinter import Frame
from Controllers.main_nav_controller import *
from Controllers.left_nav_controller import *
from Controllers.map_nav_controller import *
from Views.main_screen import *
from Models.config import *


# build config object
conf = ConfigFile()


class MainController(Frame):
    def __init__(self):

        # define view
        self.view = MainScreen()

        # build sub-controller objects
        self.left_nav_controller = LeftNavController()
        self.main_nav_controller = MainNavController()
        self.map_nav_controller = MapNavController()