# map_nav_controller.py
# description: this is the map nav controller, handles the functionality of the map in
#              the top right (not yet implemented)
#
# ApplicationController
#     IntroController
#     MainController
#         LeftNavController
#         MainNavController
#         MapNavController*

from Tkinter import Frame


class MapNavController(Frame):
    def __init__(self, parent):
        self.parent = parent
        self.app = self.parent.app

    def build_map(self):

        global main_nav
        map_nav.place(x=main_window.sw-200, y=0)
        if conf.debug == 1:
            print "Displayed: map_nav,200,200"

    def message(self, message):
        # not yet implemented
        pass