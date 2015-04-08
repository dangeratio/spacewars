from Models.config import *
from Views.main_screen import *


conf = ConfigFile()


class ApplicationController(object):
    def __init__(self, parent):
        self.main_screen = MainScreen()

    def remove_this(self):
        self.frame.destroy()

    def refresh(self):
        if self.active_view == "intro":
            self.main_screen.intro_screen.draw()
        elif self.active_view == "main":
            self.main_screen.main_nav.build()