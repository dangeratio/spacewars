from Tkinter import Frame, Canvas

class IntroScreen(Frame):
    def __init__(self, parent):     # formerly init_intro_nav():

        '''     using class objects for all these vars now
        global intro_nav, background_frame, can, button_load_game\
            , button_new_game, button_quit, intro_fill_bottom\
            , label_version, title_image_res\
            , intro_top_padding, intro_btm_padding
        '''

        self.parent = parent

        # frame setup

        background_frame = Frame(self.parent, height=self.parent.sh, width=self.parent.sw, background=self.parent.conf.window_background)
        intro_nav = Frame(background_frame, height=500, width=500, background=self.parent.conf.intro_background)

        # elements

        intro_top_padding = Canvas(intro_nav)
        intro_top_padding.configure(height=intro_padding_height, background=self.parent.conf.intro_background, highlightbackground=self.parent.conf.intro_background)

        title_image_resource = Image.open(conf.title_image_path)
        title_image_res = ImageTk.PhotoImage(title_image_resource)
        can = Canvas(intro_nav, background=self.parent.conf.intro_background, highlightbackground=self.parent.conf.intro_background)
        can.title_image_res = title_image_res
        can.config(width=title_image_res.width(), height=title_image_res.height())

        button_new_game = Button(intro_nav, text="New Game", command=event_button_new_game, bg=self.parent.conf.intro_background)
        button_new_game.config(highlightbackground=self.parent.conf.intro_background)

        button_load_game = Button(intro_nav, text="Load Game", command=event_button_load_game, bg=self.parent.conf.intro_background)
        button_load_game.config(highlightbackground=self.parent.conf.intro_background)
        button_load_game.config(state='disabled')

        button_quit = Button(intro_nav, text="Quit", command=event_button_quit, bg=self.parent.conf.intro_background)
        button_quit.config(highlightbackground=self.parent.conf.intro_background)

        label_version = Label(intro_nav, bg=self.parent.conf.intro_background, text=self.parent.conf.version)

        intro_btm_padding = Canvas(intro_nav)
        intro_btm_padding.configure(height=intro_padding_height, background=self.parent.conf.intro_background, highlightbackground=self.parent.conf.intro_background)


    def hide(self):     # formerly hide_intro_nav
        intro_nav.destroy()
        background_frame.destroy()
        can.destroy()
        button_load_game.destroy()
        button_new_game.destroy()
        button_quit.destroy()
        label_version.destroy()
        title_image_res.__del__()
        intro_top_padding.destroy()
        intro_btm_padding.destroy()

        global active_view

        if active_view == "intro":
            active_view = ""


    def draw(self):       # formerly draw_intro_nav()

        # frame setup

        if conf.debug == 1:
            pass
            # canvas = Canvas(background_frame)
            # canvas.create_line((0, 0, self.parent.sw, self.parent.sh), fill=self.parent.conf.black_color)
            # canvas.pack()

        intro_top_padding.pack()

        background_frame.pack(fill='both')
        intro_nav.pack(fill='both', padx=(self.parent.sw/2)-250, pady=(self.parent.sh/2)-250)

        if conf.debug == 1:
            print "Drew Intro, padding: (", (self.parent.sw/2)-250, ",", (self.parent.sh/2)-250, ")"

        # elements

        can.pack(fill='both', side='top', padx=50, pady=50)
        can.create_image(2, 2, image=title_image_res, anchor='nw')

        button_new_game.pack(fill="x", padx=50)
        button_load_game.pack(fill="x", padx=50)
        button_quit.pack(fill="x", padx=50)
        label_version.pack(fill='y', padx=10, pady=10)

        intro_btm_padding.pack()

        '''
        ######################################################
        #
        # remove next line for normal operation
        #
        ######################################################
        '''

        # pending_actions.append('invoke_new_game')


