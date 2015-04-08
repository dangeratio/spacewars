from models.config import *


conf = ConfigFile()

class Application():
    def __init__(self, parent):
        Frame.__init__(self, parent, background=conf.window_background)

        # Class Subs

        # future list of class subs here



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

    def remove_this(self):
        self.frame.destroy()

    def refresh(self):
        if active_view == "intro":
            draw_intro_nav()
        elif active_view == "main":
            build_main_nav()