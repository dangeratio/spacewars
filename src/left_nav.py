from configfile import *
from Tkinter import Tk, Frame, Label, Button, Canvas, CENTER
from PIL import Image, ImageTk, ImageDraw

conf = ConfigFile()


class LeftNav(Canvas):
    def __init__(self, main_window, player, left_nav):

        self.planet_images = []

        self.left_canvas = Canvas(left_nav)
        self.left_canvas.config(background=conf.left_nav_background, highlightthickness=0, height=main_window.sh, width=200)
        self.left_canvas.place(x=0, y=0)

        if conf.debug_lines == 1:
            self.left_canvas.create_line(0, 0, 200, main_window.sh, fill='red')
            self.left_canvas.create_line(200, 0, 0, main_window.sh, fill='red')

        # left nav values

        logo_image = Image.open(conf.title_image_path)
        logo_image.thumbnail([198, 48], Image.ANTIALIAS)
        logo_image_res = ImageTk.PhotoImage(logo_image)
        new_planet_image = logo_image_res
        self.planet_images.append(new_planet_image)
        label_logo = Label(self.left_canvas, image=logo_image_res)
        label_logo.config(background=conf.left_nav_background)
        label_logo.planet_image_res = logo_image_res           # keep a reference!
        label_logo.place(anchor='n', x=100, y=0)

        # build row set

        row = 0

        resources_start_y = 55
        resources_canvas = Canvas(self.left_canvas)
        resources_canvas.config(background=conf.left_nav_background,
                                height=main_window.sh-resources_start_y-202,
                                width=198,
                                highlightthickness=0,
                                border=0)
        resources_canvas.place(anchor='nw', x=0, y=resources_start_y)

        label_resources = Label(resources_canvas, text="Resources:", fg='white')
        label_resources.config(background=conf.left_nav_background)
        label_resources.grid(row=row, column=0, sticky='w')

        # row += 1
        # label_credits = Label(resources_canvas, text="Credits:", fg='grey')
        # label_credits.config(background=conf.left_nav_background)
        # label_credits.grid(row=row, column=0, sticky='w')

        # label_credits_val = Label(resources_canvas, text=player.credits, fg='grey')
        # label_credits_val.config(background=conf.left_nav_background)
        # label_credits_val.grid(row=row, column=1, sticky='e')

        row += 1
        label_planets = Label(resources_canvas, text="Planets:", fg='grey')
        label_planets.config(background=conf.left_nav_background)
        label_planets.grid(row=row, column=0, sticky='w')

        label_planets_val = Label(resources_canvas, text=str(len(player.owned_planets)), fg='grey')
        label_planets_val.config(background=conf.left_nav_background)
        label_planets_val.grid(row=row, column=1, sticky='e')

        row += 1
        label_ships = Label(resources_canvas, text="Ships:", fg='grey')
        label_ships.config(background=conf.left_nav_background)
        label_ships.grid(row=row, column=0, sticky='w')

        label_ships_val = Label(resources_canvas, text=len(player.ships), fg='grey')
        label_ships_val.config(background=conf.left_nav_background)
        label_ships_val.grid(row=row, column=1, sticky='e')

        row += 1
        label_allies = Label(resources_canvas, text="Allies:", fg='grey')
        label_allies.config(background=conf.left_nav_background)
        label_allies.grid(row=row, column=0, sticky='w')

        label_allies_val = Label(resources_canvas, text=len(player.allies), fg='grey')
        label_allies_val.config(background=conf.left_nav_background)
        label_allies_val.grid(row=row, column=1, sticky='e')

        row += 1
        label_enemies = Label(resources_canvas, text="Enemies:", fg='grey')
        label_enemies.config(background=conf.left_nav_background)
        label_enemies.grid(row=row, column=0, sticky='w')

        label_enemies_val = Label(resources_canvas, text=len(player.enemies), fg='grey')
        label_enemies_val.config(background=conf.left_nav_background)
        label_enemies_val.grid(row=row, column=1, sticky='e')

        row += 1
        label_separator = Label(resources_canvas, text="", fg='black', width=24)
        label_separator.config(background=conf.left_nav_background)
        label_separator.grid(row=row, columnspan=2, sticky='e,w')

        # left nav buttons

        left_buttons_start_y = main_window.sh-112
        left_buttons_canvas = Canvas(self.left_canvas)
        left_buttons_canvas.config(background=conf.left_nav_background,
                                   height=200,
                                   width=200,
                                   highlightthickness=0,
                                   border=0)
        left_buttons_canvas.place(anchor='n', x=100, y=left_buttons_start_y)

        button_next_planet = Button(left_buttons_canvas, text="Next Planet", padx=60
                                    , highlightbackground=conf.left_nav_background
                                    , command=self.button_next_planet_clicked)
        button_next_ship = Button(left_buttons_canvas, text="Next Ship"
                                  , highlightbackground=conf.left_nav_background
                                  , command=self.button_next_ship_clicked)
        button_home_planet = Button(left_buttons_canvas, text="Home Planet"
                                    , highlightbackground=conf.left_nav_background
                                    , command=self.button_home_planet_clicked)
        button_end_turn = Button(left_buttons_canvas, text="End Turn"
                                 , highlightbackground=conf.left_nav_background
                                 , command=self.button_end_turn_clicked)

        button_next_planet.grid(row=0, column=0, sticky='w,e')
        button_next_ship.grid(row=1, column=0, sticky='w,e')
        button_home_planet.grid(row=2, column=0, sticky='w,e')
        button_end_turn.grid(row=3, column=0, sticky='w,e')

        if conf.debug == 1:
            print "CreatedLine:", 0, " ", 0, " ", main_window.sw-200, " ", main_window.sh-200
            print "CreatedLine:", main_window.sw-200, " ", 0, " ", 0, " ", main_window.sh-200
            print "CurrWin0:", convert_coords_x(main_window, 0), convert_coords_y(main_window, 0)

        if conf.debug == 1:
            print "Displayed: left_nav,", main_window.sh, ",200"

    def button_next_planet_clicked(self):
        pass

    def button_next_ship_clicked(self):
        pass

    def button_home_planet_clicked(self):
        pass

    def button_end_turn_clicked(self):
        pass

    def redraw(self):
        pass


def convert_coords_x(main_window, x):
    return ((main_window.sw - 200) / 2) + x


def convert_coords_y(main_window, y):
    return ((main_window.sh - 200) / 2) + y


def convert_coords_name(main_window, y, size):
    return ((main_window.sh - 200) / 2) + y - (size / 2) - conf.planet_name_height


