from Tkinter import Frame


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

        self.parent = parent

        self.parent.title("space")
        # Handle click event
        # self.bind("<Button-1>", click)
        self.bind("<Configure>", resize)
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
