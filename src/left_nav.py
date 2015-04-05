from configfile import *
from Tkinter import Tk, Frame, Label, Button, Canvas, CENTER, CURRENT, Listbox, END
from PIL import Image, ImageTk, ImageDraw
from popup import *


conf = ConfigFile()


class LeftNav(Canvas):

    def __init__(self, main_window, player_, left_nav):

        self.selected_planet = player_.selected_planet
        if isset(player_.selected_ship):
            self.selected_ship_name = player_.selected_ship.name
        else:
            self.selected_ship_name = ""

        self.player = player_
        self.main_window = main_window
        self.parent = left_nav

        self.planet_images = []

        self.left_canvas = Canvas(left_nav)
        self.left_canvas.config(background=conf.left_nav_background, highlightthickness=0, height=main_window.sh, width=200)
        self.left_canvas.place(x=0, y=0)

        if conf.debug_lines == 1:
            self.left_canvas.create_line(0, 0, 200, main_window.sh, fill='red')
            self.left_canvas.create_line(200, 0, 0, main_window.sh, fill='red')

        # left nav values

        self.logo_image = Image.open(conf.title_image_path)
        self.logo_image.thumbnail([198, 48], Image.ANTIALIAS)
        self.logo_image_res = ImageTk.PhotoImage(self.logo_image)
        self.new_planet_image = self.logo_image_res
        self.planet_images.append(self.new_planet_image)
        self.label_logo = Label(self.left_canvas, image=self.logo_image_res)
        self.label_logo.config(background=conf.left_nav_background)
        self.label_logo.planet_image_res = self.logo_image_res           # keep a reference!
        self.label_logo.place(anchor='n', x=100, y=0)

        # Resources Set
        row = 0
        self.resources_start_y = 55
        self.resources_canvas = Canvas(self.left_canvas)
        self.resources_canvas.config(background=conf.left_nav_background,
                                     width=198,
                                     highlightthickness=0,
                                     border=0)
        self.resources_canvas.grid_propagate(False)

        self.resources_canvas.place(anchor='nw', x=0, y=self.resources_start_y)
        self.label_resources = Label(self.resources_canvas, text="Resources:", fg=conf.main_text_color)
        self.label_resources.config(background=conf.left_nav_background)
        self.label_resources.grid(row=row, column=0, sticky='w')
        row += 1
        self.label_planets = Label(self.resources_canvas, text="Planets:", fg=conf.second_text_color)
        self.label_planets.config(background=conf.left_nav_background)
        self.label_planets.grid(row=row, column=0, sticky='w')
        self.label_planets_val = Label(self.resources_canvas, text=str(len(self.player.owned_planets))
                                       , fg=conf.second_text_color)
        self.label_planets_val.config(background=conf.left_nav_background)
        self.label_planets_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_ships = Label(self.resources_canvas, text="Ships:", fg=conf.second_text_color)
        self.label_ships.config(background=conf.left_nav_background)
        self.label_ships.grid(row=row, column=0, sticky='w')
        self.label_ships_val = Label(self.resources_canvas, text=len(self.player.ships), fg=conf.second_text_color)
        self.label_ships_val.config(background=conf.left_nav_background)
        self.label_ships_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_allies = Label(self.resources_canvas, text="Allies:", fg=conf.second_text_color)
        self.label_allies.config(background=conf.left_nav_background)
        self.label_allies.grid(row=row, column=0, sticky='w')
        self.label_allies_val = Label(self.resources_canvas, text=len(self.player.allies), fg=conf.second_text_color)
        self.label_allies_val.config(background=conf.left_nav_background)
        self.label_allies_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_enemies = Label(self.resources_canvas, text="Enemies:", fg=conf.second_text_color)
        self.label_enemies.config(background=conf.left_nav_background)
        self.label_enemies.grid(row=row, column=0, sticky='w')
        self.label_enemies_val = Label(self.resources_canvas, text=len(self.player.enemies), fg=conf.second_text_color)
        self.label_enemies_val.config(background=conf.left_nav_background)
        self.label_enemies_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_separator = Label(self.resources_canvas, text="", fg=conf.left_nav_background, width=24)
        self.label_separator.config(background=conf.left_nav_background)
        self.label_separator.grid(row=row, columnspan=2, sticky='e,w')

        # left nav buttons
        self.left_buttons_start_y = main_window.sh-112
        if self.left_buttons_start_y < 500:
            self.left_buttons_start_y = 500

        self.left_buttons_canvas = Canvas(self.left_canvas)
        self.left_buttons_canvas.config(background=conf.left_nav_background,
                                        height=200,
                                        width=200,
                                        highlightthickness=0,
                                        border=0)
        self.left_buttons_canvas.place(anchor='n', x=100, y=self.left_buttons_start_y)

        self.button_next_planet = Button(self.left_buttons_canvas, text="Next Planet", padx=60
                                         , highlightbackground=conf.left_nav_background)
        self.button_next_ship = Button(self.left_buttons_canvas, text="Next Ship"
                                       , highlightbackground=conf.left_nav_background)
        self.button_home_planet = Button(self.left_buttons_canvas, text="Home Planet"
                                         , highlightbackground=conf.left_nav_background)
        self.button_end_turn = Button(self.left_buttons_canvas, text="End Turn"
                                      , highlightbackground=conf.left_nav_background)
        self.button_next_planet.bind("<Button-1>", button_next_planet_clicked)
        self.button_next_ship.bind("<Button-1>", button_next_ship_clicked)
        self.button_home_planet.bind("<Button-1>", button_home_planet_clicked)
        self.button_end_turn.bind("<Button-1>", button_end_turn_clicked)
        self.button_next_planet.grid(row=0, column=0, sticky='w,e')
        self.button_next_ship.grid(row=1, column=0, sticky='w,e')
        self.button_home_planet.grid(row=2, column=0, sticky='w,e')
        self.button_end_turn.grid(row=3, column=0, sticky='w,e')

        # Planet Info Set

        row = 0
        self.planet_info_start_y = self.resources_start_y + 115
        self.planet_info_canvas = Canvas(self.left_canvas)
        self.planet_info_canvas.config(background=conf.left_nav_background,
                                       width=198,
                                       highlightthickness=0,
                                       border=0)
        self.planet_info_canvas.grid_propagate(False)
        self.planet_info_canvas.place(anchor='nw', x=0, y=self.planet_info_start_y)
        self.label_planet_info = Label(self.planet_info_canvas, text="Planet Info:", fg=conf.main_text_color)
        self.label_planet_info.config(background=conf.left_nav_background)
        self.label_planet_info.grid(row=row, column=0, sticky='w')
        row += 1
        self.label_planet_name = Label(self.planet_info_canvas, text="Name:", fg=conf.second_text_color)
        self.label_planet_name.config(background=conf.left_nav_background)
        self.label_planet_name.grid(row=row, column=0, sticky='w')
        self.label_planet_name_val = Label(self.planet_info_canvas, text=self.player.selected_planet.name
                                           , fg=conf.second_text_color)
        self.label_planet_name_val.config(background=conf.left_nav_background)
        self.label_planet_name_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_planet_metals = Label(self.planet_info_canvas, text="Metals:", fg=conf.second_text_color)
        self.label_planet_metals.config(background=conf.left_nav_background)
        self.label_planet_metals.grid(row=row, column=0, sticky='w')
        self.label_planet_metals_val = Label(self.planet_info_canvas, text=self.player.selected_planet.metals
                                             , fg=conf.second_text_color)
        self.label_planet_metals_val.config(background=conf.left_nav_background)
        self.label_planet_metals_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_planet_food = Label(self.planet_info_canvas, text="Food:", fg=conf.second_text_color)
        self.label_planet_food.config(background=conf.left_nav_background)
        self.label_planet_food.grid(row=row, column=0, sticky='w')
        self.label_planet_food_val = Label(self.planet_info_canvas, text=self.player.selected_planet.food
                                           , fg=conf.second_text_color)
        self.label_planet_food_val.config(background=conf.left_nav_background)
        self.label_planet_food_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_planet_terrain = Label(self.planet_info_canvas, text="Terrain:", fg=conf.second_text_color)
        self.label_planet_terrain.config(background=conf.left_nav_background)
        self.label_planet_terrain.grid(row=row, column=0, sticky='w')
        self.label_planet_terrain_val = Label(self.planet_info_canvas, text=get_terrain(self.player.selected_planet.terrain)
                                              , fg=conf.second_text_color)
        self.label_planet_terrain_val.config(background=conf.left_nav_background)
        self.label_planet_terrain_val.grid(row=row, column=1, sticky='e')

        # ship info

        row = 0
        self.ship_info_start_y = self.planet_info_start_y + 115
        self.ship_info_canvas = Canvas(self.left_canvas)
        self.ship_info_canvas.config(background=conf.left_nav_background,
                                     width=198,
                                     highlightthickness=0,
                                     border=0)
        self.ship_info_canvas.grid_propagate(False)
        self.ship_info_canvas.place(anchor='nw', x=0, y=self.ship_info_start_y)
        self.label_ship_info = Label(self.ship_info_canvas, text="Ship Info:", fg=conf.main_text_color)
        self.label_ship_info.config(background=conf.left_nav_background)
        self.label_ship_info.grid(row=row, column=0, sticky='w')

        # future implementation

        # if selected_ship.name != '':
        if isset(self.player.selected_ship) != '' and self.player.selected_ship != 0:
            row += 1
            self.label_ship_name = Label(self.ship_info_canvas, text="Name:", fg=conf.second_text_color)
            self.label_ship_name.config(background=conf.left_nav_background)
            self.label_ship_name.grid(row=row, column=0, sticky='w')
            self.label_ship_name_val = Label(self.planet_info_canvas, text=self.player.selected_ship.name, fg=conf.second_text_color)
            self.label_ship_name_val.config(background=conf.left_nav_background)
            self.label_ship_name_val.grid(row=row, column=1, sticky='e')
        else:
            row += 1
            self.label_ship_name = Label(self.ship_info_canvas, text="No Ship Selected", fg=conf.second_text_color)
            self.label_ship_name.config(background=conf.left_nav_background)
            self.label_ship_name.grid(row=row, columnspan=2, sticky='w')
            row += 1
            self.listbox_ship = Listbox(self.ship_info_canvas)
            for ship in self.player.ships:
                self.listbox_ship.insert(END, ship.name)
            self.listbox_ship.after(250, self.poll_ship_list)









        row += 1
        self.label_separator = Label(self.planet_info_canvas, text="", fg=conf.left_nav_background, width=24)
        self.label_separator.config(background=conf.left_nav_background)
        self.label_separator.grid(row=row, columnspan=2, sticky='e,w')


        if conf.debug == 1:
            print "CreatedLine:", 0, " ", 0, " ", main_window.sw-200, " ", main_window.sh-200
            print "CreatedLine:", main_window.sw-200, " ", 0, " ", 0, " ", main_window.sh-200
            print "CurrWin0:", convert_coords_x(main_window, 0), convert_coords_y(main_window, 0)

        if conf.debug == 1:
            print "Displayed: left_nav,", main_window.sh, ",200"

    def poll_ship_list(self):
        new_ship_name = self.listbox_ship.curselection()
        if isset(self.selected_ship_name):
            if self.selected_ship_name == "":
                if new_ship_name != self.selected_ship_name:
                    self.ship_selction_has_changed(new_ship_name)
                    self.selected_ship_name = new_ship_name
        self.main_window.after(250, self.poll_ship_list)

    def ship_selction_has_changed(self, new_ship_name):
        print "ShipSelection:", new_ship_name

    def redraw(self, main_window, player):

        self.player = player


        if conf.debug == 1:
            print "Redrawing Left Nav"

        self.label_logo.place(anchor='n', x=100, y=0)
        self.resources_canvas.config(background=conf.left_nav_background,
                                     height=main_window.sh-self.resources_start_y-202,
                                     width=198,
                                     highlightthickness=0,
                                     border=0)
        self.resources_canvas.place(anchor='nw', x=0, y=self.resources_start_y)
        row = 0
        self.label_resources.grid(row=row, column=0, sticky='w')
        row += 1
        self.label_planets.grid(row=row, column=0, sticky='w')
        self.label_planets_val.config(text=str(len(self.player.owned_planets)))
        self.label_planets_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_ships.grid(row=row, column=0, sticky='w')
        self.label_ships_val.config(text=len(self.player.ships))
        self.label_ships_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_allies.grid(row=row, column=0, sticky='w')
        self.label_allies_val.config(text=len(self.player.allies))
        self.label_allies_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_enemies.grid(row=row, column=0, sticky='w')
        self.label_enemies_val.config(text=len(self.player.enemies))
        self.label_enemies_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_separator.grid(row=row, columnspan=2, sticky='e,w')

        # left nav buttons

        self.left_buttons_start_y = main_window.sh-112
        if self.left_buttons_start_y < 500:
            self.left_buttons_start_y = 500
        self.left_buttons_canvas.place(anchor='n', x=100, y=self.left_buttons_start_y)
        self.button_next_planet.grid(row=0, column=0, sticky='w,e')
        self.button_next_ship.grid(row=1, column=0, sticky='w,e')
        self.button_home_planet.grid(row=2, column=0, sticky='w,e')
        self.button_end_turn.grid(row=3, column=0, sticky='w,e')

        if conf.debug == 1:
            print "Left Buttons Start Y:", self.left_buttons_start_y



def convert_coords_x(main_window, x):
    return ((main_window.sw - 200) / 2) + x


def convert_coords_y(main_window, y):
    return ((main_window.sh - 200) / 2) + y


def convert_coords_name(main_window, y, size):
    return ((main_window.sh - 200) / 2) + y - (size / 2) - conf.planet_name_height


def button_next_planet_clicked(event):
    if conf.debug == 1:
        print "Next Planet Clicked"
    popup = Popup('', 'text', 'button')
    frame_obj = event.widget.master.master.master.master

    popup.display(frame_obj)


def dismiss_popup(event):
    event.widget.master.delete()


def button_next_ship_clicked(event):
    if conf.debug == 1:
        print "Next Ship Clicked"
    pass


def button_home_planet_clicked(event):
    if conf.debug == 1:
        print "Home Planet Clicked"
    pass


def button_end_turn_clicked(event):
    if conf.debug == 1:
        print "End Turn Clicked"
    pass


def get_terrain(terrain):
    if terrain == 1:
        return 'Ice'
    elif terrain == 2:
        return 'Rock'
    elif terrain == 3:
        return 'Green'
    elif terrain == 4:
        return 'Water'
    elif terrain == 5:
        return 'Alien'
    else:
        return 'Black'


def isset(variable):
    return variable in locals() or variable in globals()
