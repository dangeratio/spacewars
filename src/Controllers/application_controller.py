# application_controller.py
# description: this is the main controller object with all other controller objects under it
#
# ApplicationController*
#     IntroController
#     MainController
#         LeftNavController
#         MainNavController
#         MapNavController


from Models.config import *
from Models.game import *
from Views.main_screen import *
from Controllers.main_controller import *
from Controllers.intro_controller import *


class ApplicationController(object):
    def __init__(self):

        # save config
        self.conf = ConfigFile()

        # build intro screen controller to handle intro screen requests
        self.intro_controller = IntroController(self)

        # build main controller to handle main screen requests
        self.main_controller = MainController(self)

        # initiate main screen - now handled within the respective controllers (initiated above)
        # self.main_screen = MainScreen(self.main_controller, 'intro')       # initiate the main screen with the intro
        # self.main_screen = MainScreen(self.root, 'main')        # initiate the main screen, skipping the intro

    def remove_this(self):
        self.frame.destroy()

    def refresh(self):
        if self.active_view == "intro":
            self.main_screen.intro_screen.draw()
        elif self.active_view == "main":
            self.main_screen.main_nav.build()


# replace this function using x in array_of_x if/then statement, python is probably more efficent than I am :)

def add_unique(array, item):

    in_array = False
    for i in array:
        if i == item:
            in_array = True

    if not in_array:
        array.append(item)

    return array