from Tkinter import Tk, Frame


class MainView(Frame):
    def __init__(self, controller):

        # connect up controller
        self.controller = controller
        self.app = self.controller.app

        # initial window setup
        self.root = Tk()
        Frame.__init__(self, self.root, background=self.app.conf.window_background)
        self.root.title("space")

        # window resize event
        self.bind("<Configure>", self.resize)
        self.pack(fill='both', expand=1)

        # initial window size, setup, creation
        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()
        self.update()
        self.root.geometry('%dx%d+%d+%d' % (self.sw, self.sh, 0, 0))


    def resize(self, event):

        self.sw = event.width
        self.sh = event.height

        if self.sw <= 500:
            self.sw = 500

        if self.sh <= 500:
            self.sh = 500

        if self.app.conf.debug == 1:
            print "(", self.sw, ",", self.sh, ")"

        self.refresh()

    def refresh(self):

        self.controller.broadcast('refresh')

        '''

        if self.active_view == "intro":
            self.main_screen.intro_screen.draw()
        elif self.active_view == "main":
            self.main_screen.main_nav.build()

        '''

