from Tkinter import Frame
from Views.intro_screen import *
from Views.main_nav import *
from Views.left_nav import *
from Views.map import *
from Views.popup import *


class MainScreen(Frame):
    def __init__(self, controller, initial_view):

        # connect up controller
        self.controller = controller

        # initial window setup
        self.root = Tk()
        Frame.__init__(self, self.root, background=conf.window_background)
        self.root.title("space")

        # child object references
        self.intro_screen = 0
        self.main_nav = 0
        self.left_nav = 0
        self.map_nav = 0

        # window resize event
        self.bind("<Configure>", self.resize)
        self.pack(fill='both', expand=1)

        # initial window size, setup, creation
        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()
        self.update()
        self.root.geometry('%dx%d+%d+%d' % (self.sw, self.sh, 0, 0))
        self.initial_view = initial_view
        self.display(initial_view)

        # enter root runloop
        self.root.mainloop()

    def display(self, view):

        if view == 'intro':
            self.intro_screen = IntroScreen(self.controller.main_controller.intro_controller, self)
        elif view == 'main':
            # create nav's for the main view
            self.main_nav = MainNav()
            self.left_nav = LeftNav()
            # self.map_nav = MapNav()       # not yet implemented

    def resize(self, event):

        self.sw = event.width
        self.sh = event.height

        if self.sw <= 500:
            self.sw = 500

        if self.sh <= 500:
            self.sh = 500

        if conf.debug == 1:
            print "(", self.sw, ",", self.sh, ",", self.initial_view, ")"

        self.refresh()


    def build_left_nav_menu(self):

        global left_nav, left_canvas, left

        left_nav.place(x=0, y=0)

        left = LeftNav(main_window, player, left_nav)

    def build_map(self):

        global main_nav
        map_nav.place(x=main_window.sw-200, y=0)
        if conf.debug == 1:
            print "Displayed: map_nav,200,200"