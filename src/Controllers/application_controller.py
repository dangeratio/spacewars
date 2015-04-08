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
from Views.main_screen import *


conf = ConfigFile()


class ApplicationController(object):
    def __init__(self, parent):
        self.main_screen = MainScreen()
        self.intro_controller = IntroController()

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