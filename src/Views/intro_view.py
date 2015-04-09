from Tkinter import Frame, Canvas, Button, Label
from PIL import Image, ImageTk



class IntroView(Frame):
    def __init__(self, controller, parent):     # formerly init_intro_nav():

        '''     using class objects for all these vars now
        global intro_nav, background_frame, can, button_load_game\
            , button_new_game, button_quit, intro_fill_bottom\
            , label_version, title_image_res\
            , intro_top_padding, intro_btm_padding
        '''

        self.controller = controller
        self.parent = parent
        self.app = self.controller.app

        # declare vars

        self.background_frame = 0
        self.intro_nav = 0
        self.intro_top_padding = 0

    def build(self):        # prev: build_intro_nav

        # frame setup
        conf = self.app.conf

        self.background_frame = Frame(self.parent, height=self.parent.sh, width=self.parent.sw
                                      , background=conf.window_background)
        self.intro_nav = Frame(self.background_frame, height=500, width=500
                               , background=conf.intro_background)

        # elements

        self.intro_top_padding = Canvas(self.intro_nav)
        self.intro_top_padding.configure(height=conf.intro_padding_height
                                         , background=conf.intro_background
                                         , highlightbackground=conf.intro_background)

        self.title_image_resource = Image.open(conf.title_image_path)
        self.title_image_res = ImageTk.PhotoImage(self.title_image_resource)
        self.can = Canvas(self.intro_nav, background=conf.intro_background
                          , highlightbackground=conf.intro_background)
        self.can.title_image_res = self.title_image_res
        self.can.config(width=self.title_image_res.width(), height=self.title_image_res.height())

        self.button_new_game = Button(self.intro_nav, text="New Game"
                                      , command=self.controller.event_button_new_game
                                      , bg=conf.intro_background)
        self.button_new_game.config(highlightbackground=conf.intro_background)

        self.button_load_game = Button(self.intro_nav, text="Load Game"
                                       , command=self.controller.event_button_load_game
                                       , bg=conf.intro_background)
        self.button_load_game.config(highlightbackground=conf.intro_background)
        self.button_load_game.config(state='disabled')

        self.button_quit = Button(self.intro_nav, text="Quit"
                                  , command=self.controller.event_button_quit
                                  , bg=conf.intro_background)
        self.button_quit.config(highlightbackground=conf.intro_background)

        self.label_version = Label(self.intro_nav, bg=conf.intro_background, text=conf.version)

        self.intro_btm_padding = Canvas(self.intro_nav)
        self.intro_btm_padding.configure(height=conf.intro_padding_height
                                         , background=conf.intro_background
                                         , highlightbackground=conf.intro_background)

    def hide(self):     # formerly hide_intro_nav
        self.intro_nav.destroy()
        self.background_frame.destroy()
        self.can.destroy()
        self.button_load_game.destroy()
        self.button_new_game.destroy()
        self.button_quit.destroy()
        self.label_version.destroy()
        self.title_image_res.__del__()
        self.intro_top_padding.destroy()
        self.intro_btm_padding.destroy()


    def draw(self):       # formerly draw_intro_nav()

        # frame setup

        self.intro_top_padding.pack()

        self.background_frame.pack(fill='both')
        self.intro_nav.pack(fill='both', padx=(self.parent.sw/2)-250, pady=(self.parent.sh/2)-250)

        self.app.debug(("Drew Intro, padding: (", (self.parent.sw/2)-250, ",", (self.parent.sh/2)-250, ")"))

        # elements

        self.can.pack(fill='both', side='top', padx=50, pady=50)
        self.can.create_image(2, 2, image=self.title_image_res, anchor='nw')

        self.button_new_game.pack(fill="x", padx=50)
        self.button_load_game.pack(fill="x", padx=50)
        self.button_quit.pack(fill="x", padx=50)
        self.label_version.pack(fill='y', padx=10, pady=10)

        self.intro_btm_padding.pack()

        '''
        ######################################################
        #
        # remove next line for normal operation
        #
        ######################################################
        '''

        # pending_actions.append('invoke_new_game')


