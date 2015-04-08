from Tkinter import Frame
from Views.intro_screen import *
from Views.main_nav import *
from Views.left_nav import *
from Views.map import *
from Views.popup import *


class MainScreen(Frame):
    def __init__(self, parent):

        Frame.__init__(self, parent, background=conf.window_background)

        # Class Subs
        #
        # future list of class subs here
        #
        #
        #
        #

        self.intro_screen = IntroScreen()

        # original code to add a left nav to the window


        self.parent = parent

        self.parent.title("space")
        # Handle click event
        # self.bind("<Button-1>", click)
        self.bind("<Configure>", self.resize)
        self.pack(fill='both', expand=1)

        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()

        self.update()

        # un init-ed vars
        self.active_view = ''

        self.parent.geometry('%dx%d+%d+%d' % (self.sw, self.sh, 0, 0))

        '''
        active_view variable controls what view is displayed.  These are the values:
        - intro: this is the first screen a user sees when they enter the game
        - main: this is the main game screen the user will spend most of the time in the game playing
        '''

        self.active_view = "intro"

    def resize(self, event):

        global main_window
        global active_view

        main_window.sw = event.width
        main_window.sh = event.height

        if main_window.sw <= 500:
            main_window.sw = 500

        if main_window.sh <= 500:
            main_window.sh = 500

        if conf.debug == 1:
            print "(", main_window.sw, ",", main_window.sh, ",", active_view, ")"

        main_window.refresh()


    def build_left_nav_menu(self):

        global left_nav, left_canvas, left

        left_nav.place(x=0, y=0)

        left = LeftNav(main_window, player, left_nav)

    def build_map(self):

        global main_nav
        map_nav.place(x=main_window.sw-200, y=0)
        if conf.debug == 1:
            print "Displayed: map_nav,200,200"