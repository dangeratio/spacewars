from Tkinter import Tk, Frame, Label, Button, Canvas, CENTER, CURRENT, Listbox, END, SINGLE
from PIL import Image, ImageTk, ImageDraw


class LeftNavView(Canvas):

    def __init__(self, controller, parent):     # prev: def __init__(self, main_window, player_, left_nav):
        self.controller = controller
        self.parent = parent
        self.enabled = False

    def build(self):

        if self.enabled:
            self.redraw()
        else:
            self.build_left_nav_menu()
            self.enabled = True

    def build_left_nav_menu(self):

        app = self.app
        main_window = app.main_controller.view
        player = app.game.player

        left_nav = Frame(main_window, height=main_window.sh, width=200, background=app.app.confleft_nav_background)

        self.selected_planet = player.selected_planet
        if isset(player.selected_ship):
            self.selected_ship_name = player.selected_ship.name
        else:
            self.selected_ship_name = ""

        self.main_window = main_window
        self.selected_ship_id = 0

        self.planet_images = []

        self.left_canvas = Canvas(left_nav)
        self.left_canvas.config(background=app.confleft_nav_background, highlightthickness=0, height=main_window.sh, width=200)
        self.left_canvas.place(x=0, y=0)

        if app.confdebug_lines == 1:
            self.left_canvas.create_line(0, 0, 200, main_window.sh, fill='red')
            self.left_canvas.create_line(200, 0, 0, main_window.sh, fill='red')

        # left nav values

        self.logo_image = Image.open(app.conftitle_image_path)
        self.logo_image.thumbnail([198, 48], Image.ANTIALIAS)
        self.logo_image_res = ImageTk.PhotoImage(self.logo_image)
        self.new_planet_image = self.logo_image_res
        self.planet_images.append(self.new_planet_image)
        self.label_logo = Label(self.left_canvas, image=self.logo_image_res)
        self.label_logo.config(background=app.confleft_nav_background)
        self.label_logo.planet_image_res = self.logo_image_res           # keep a reference!
        self.label_logo.place(anchor='n', x=100, y=0)

        # Resources Set
        row = 0
        self.resources_start_y = 55
        self.resources_canvas = Canvas(self.left_canvas)
        self.resources_canvas.config(background=app.confleft_nav_background,
                                     width=198,
                                     highlightthickness=0,
                                     border=0)
        self.resources_canvas.grid_propagate(False)

        self.resources_canvas.place(anchor='nw', x=0, y=self.resources_start_y)
        self.label_resources = Label(self.resources_canvas, text="Resources:", fg=app.confmain_text_color)
        self.label_resources.config(background=app.confleft_nav_background)
        self.label_resources.grid(row=row, column=0, sticky='w')
        row += 1
        self.label_planets = Label(self.resources_canvas, text="Planets:", fg=app.confsecond_text_color)
        self.label_planets.config(background=app.confleft_nav_background)
        self.label_planets.grid(row=row, column=0, sticky='w')
        self.label_planets_val = Label(self.resources_canvas, text=str(len(self.player.owned_planets))
                                       , fg=app.confsecond_text_color)
        self.label_planets_val.config(background=app.confleft_nav_background)
        self.label_planets_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_ships = Label(self.resources_canvas, text="Ships:", fg=app.confsecond_text_color)
        self.label_ships.config(background=app.confleft_nav_background)
        self.label_ships.grid(row=row, column=0, sticky='w')
        self.label_ships_val = Label(self.resources_canvas, text=len(self.player.ships), fg=app.confsecond_text_color)
        self.label_ships_val.config(background=app.confleft_nav_background)
        self.label_ships_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_allies = Label(self.resources_canvas, text="Allies:", fg=app.confsecond_text_color)
        self.label_allies.config(background=app.confleft_nav_background)
        self.label_allies.grid(row=row, column=0, sticky='w')
        self.label_allies_val = Label(self.resources_canvas, text=len(self.player.allies), fg=app.confsecond_text_color)
        self.label_allies_val.config(background=app.confleft_nav_background)
        self.label_allies_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_enemies = Label(self.resources_canvas, text="Enemies:", fg=app.confsecond_text_color)
        self.label_enemies.config(background=app.confleft_nav_background)
        self.label_enemies.grid(row=row, column=0, sticky='w')
        self.label_enemies_val = Label(self.resources_canvas, text=len(self.player.enemies), fg=app.confsecond_text_color)
        self.label_enemies_val.config(background=app.confleft_nav_background)
        self.label_enemies_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_separator = Label(self.resources_canvas, text="", fg=app.confleft_nav_background, width=24)
        self.label_separator.config(background=app.confleft_nav_background)
        self.label_separator.grid(row=row, columnspan=2, sticky='e,w')

        # left nav buttons
        self.left_buttons_start_y = main_window.sh-112
        if self.left_buttons_start_y < 500:
            self.left_buttons_start_y = 500

        self.left_buttons_canvas = Canvas(self.left_canvas)
        self.left_buttons_canvas.config(background=app.confleft_nav_background,
                                        height=200,
                                        width=200,
                                        highlightthickness=0,
                                        border=0)
        self.left_buttons_canvas.place(anchor='n', x=100, y=self.left_buttons_start_y)

        self.button_next_planet = Button(self.left_buttons_canvas, text="Next Planet", padx=60
                                         , highlightbackground=app.confleft_nav_background)
        self.button_next_ship = Button(self.left_buttons_canvas, text="Next Ship"
                                       , highlightbackground=app.confleft_nav_background)
        self.button_home_planet = Button(self.left_buttons_canvas, text="Home Planet"
                                         , highlightbackground=app.confleft_nav_background)
        self.button_end_turn = Button(self.left_buttons_canvas, text="End Turn"
                                      , highlightbackground=app.confleft_nav_background)
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
        self.planet_info_canvas.config(background=app.confleft_nav_background,
                                       width=198,
                                       highlightthickness=0,
                                       border=0)
        self.planet_info_canvas.grid_propagate(False)
        self.planet_info_canvas.place(anchor='nw', x=0, y=self.planet_info_start_y)
        self.label_planet_info = Label(self.planet_info_canvas, text="Planet Info:", fg=app.confmain_text_color)
        self.label_planet_info.config(background=app.confleft_nav_background)
        self.label_planet_info.grid(row=row, column=0, sticky='w')
        row += 1
        self.label_planet_name = Label(self.planet_info_canvas, text="Name:", fg=app.confsecond_text_color)
        self.label_planet_name.config(background=app.confleft_nav_background)
        self.label_planet_name.grid(row=row, column=0, sticky='w')
        self.label_planet_name_val = Label(self.planet_info_canvas, text=str(self.player.selected_planet.name)
                                           , fg=app.confsecond_text_color)
        self.label_planet_name_val.config(background=app.confleft_nav_background)
        self.label_planet_name_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_planet_metals = Label(self.planet_info_canvas, text="Metals:", fg=app.confsecond_text_color)
        self.label_planet_metals.config(background=app.confleft_nav_background)
        self.label_planet_metals.grid(row=row, column=0, sticky='w')
        self.label_planet_metals_val = Label(self.planet_info_canvas, text=str(self.player.selected_planet.metals)
                                             , fg=app.confsecond_text_color)
        self.label_planet_metals_val.config(background=app.confleft_nav_background)
        self.label_planet_metals_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_planet_food = Label(self.planet_info_canvas, text="Food:", fg=app.confsecond_text_color)
        self.label_planet_food.config(background=app.confleft_nav_background)
        self.label_planet_food.grid(row=row, column=0, sticky='w')
        self.label_planet_food_val = Label(self.planet_info_canvas, text=str(self.player.selected_planet.food)
                                           , fg=app.confsecond_text_color)
        self.label_planet_food_val.config(background=app.confleft_nav_background)
        self.label_planet_food_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_planet_terrain = Label(self.planet_info_canvas, text="Terrain:", fg=app.confsecond_text_color)
        self.label_planet_terrain.config(background=app.confleft_nav_background)
        self.label_planet_terrain.grid(row=row, column=0, sticky='w')
        self.label_planet_terrain_val = Label(self.planet_info_canvas, text=str(get_terrain(self.player.selected_planet.terrain))
                                              , fg=app.confsecond_text_color)
        self.label_planet_terrain_val.config(background=app.confleft_nav_background)
        self.label_planet_terrain_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_separator_p = Label(self.planet_info_canvas, text="", fg=app.confleft_nav_background, width=24)
        self.label_separator_p.config(background=app.confleft_nav_background)
        self.label_separator_p.grid(row=row, columnspan=2, sticky='e,w')

        # ship info

        row = 0
        self.ship_select_start_y = self.planet_info_start_y + 115
        self.ship_select_canvas = Canvas(self.left_canvas)
        self.ship_select_canvas.config(background=app.confleft_nav_background,
                                       width=198,
                                       highlightthickness=0,
                                       border=0)
        self.ship_select_canvas.grid_propagate(False)
        self.ship_select_canvas.place(anchor='nw', x=0, y=self.ship_select_start_y)
        self.label_ship_select = Label(self.ship_select_canvas, text="Select Ship:", fg=app.confmain_text_color)
        self.label_ship_select.config(background=app.confleft_nav_background)
        self.label_ship_select.grid(row=row, column=0, sticky='w')

        # future implementation

        # if selected_ship.name != '':
        if isset(self.selected_ship_name):

            if app.confdebug == 1:
                print "Showing Selected Ship (init)"

            current_ship = self.player.get_ship(self.selected_ship_name)

            row += 1
            self.listbox_ship = Listbox(self.ship_select_canvas, width=198
                                        , background=app.confalternate_left_nav_background, borderwidth=1)
            self.listbox_ship.config(selectmode=SINGLE)
            for ship in self.player.ships:
                self.listbox_ship.insert(END, ship.name)
            self.listbox_ship.selection_set(self.selected_ship_id)
            self.listbox_ship.grid(row=row, columnspan=4, sticky='w,e')
            self.listbox_ship.bind('<<ListboxSelect>>', self.poll_ship_list)

            row = 0
            self.ship_info_start_y = self.ship_select_start_y + 200
            self.ship_info_canvas = Canvas(self.left_canvas)
            self.ship_info_canvas.config(background=app.confleft_nav_background,
                                         width=198,
                                         highlightthickness=0,
                                         border=0)
            self.ship_info_canvas.grid_propagate(False)
            self.ship_info_canvas.place(anchor='nw', x=0, y=self.ship_info_start_y)
            self.label_ship_info = Label(self.ship_info_canvas, text="Ship Info:", fg=app.confmain_text_color)
            self.label_ship_info.config(background=app.confleft_nav_background)
            self.label_ship_info.grid(row=row, column=0, sticky='w')

            row += 1
            self.label_ship_name = Label(self.ship_info_canvas, text="Name:", fg=app.confsecond_text_color)
            self.label_ship_name.config(background=app.confleft_nav_background)
            self.label_ship_name.grid(row=row, column=0, columnspan=2, sticky='w')
            self.label_ship_name_val = Label(self.ship_info_canvas, text=current_ship.name
                                             , fg=app.confsecond_text_color)
            self.label_ship_name_val.config(background=app.confleft_nav_background)
            self.label_ship_name_val.grid(row=row, column=2, columnspan=2, sticky='e')

            row += 1
            self.label_ship_attack = Label(self.ship_info_canvas, text="Attack:", fg=app.confsecond_text_color)
            self.label_ship_attack.config(background=app.confleft_nav_background)
            self.label_ship_attack.grid(row=row, column=0, sticky='w')
            self.label_ship_attack_val = Label(self.ship_info_canvas, text=current_ship.attack
                                             , fg=app.confsecond_text_color)
            self.label_ship_attack_val.config(background=app.confleft_nav_background)
            self.label_ship_attack_val.grid(row=row, column=1, sticky='e')
            self.label_ship_defense = Label(self.ship_info_canvas, text="Defense:", fg=app.confsecond_text_color)
            self.label_ship_defense.config(background=app.confleft_nav_background)
            self.label_ship_defense.grid(row=row, column=2, sticky='w')
            self.label_ship_defense_val = Label(self.ship_info_canvas, text=current_ship.defense
                                             , fg=app.confsecond_text_color)
            self.label_ship_defense_val.config(background=app.confleft_nav_background)
            self.label_ship_defense_val.grid(row=row, column=3, sticky='e')

            row += 1
            self.label_ship_storage = Label(self.ship_info_canvas, text="Storage:", fg=app.confsecond_text_color)
            self.label_ship_storage.config(background=app.confleft_nav_background)
            self.label_ship_storage.grid(row=row, column=0, columnspan=2, sticky='w')
            self.label_ship_storage_val = Label(self.ship_info_canvas, text=current_ship.storage
                                             , fg=app.confsecond_text_color)
            self.label_ship_storage_val.config(background=app.confleft_nav_background)
            self.label_ship_storage_val.grid(row=row, column=2, columnspan=2, sticky='e')

            row += 1
            self.label_ship_seats = Label(self.ship_info_canvas, text="Seats:", fg=app.confsecond_text_color)
            self.label_ship_seats.config(background=app.confleft_nav_background)
            self.label_ship_seats.grid(row=row, column=0, columnspan=2, sticky='w')
            self.label_ship_seats_val = Label(self.ship_info_canvas, text=current_ship.seats
                                             , fg=app.confsecond_text_color)
            self.label_ship_seats_val.config(background=app.confleft_nav_background)
            self.label_ship_seats_val.grid(row=row, column=2, columnspan=2, sticky='e')

            row += 1
            self.label_separator_s = Label(self.ship_info_canvas, text="", fg=app.confleft_nav_background, width=24)
            self.label_separator_s.config(background=app.confleft_nav_background)
            self.label_separator_s.grid(row=row, columnspan=4, sticky='e,w')

        else:

            if app.confdebug == 1:
                print "No Selected Ship Detected (init)"

            row += 1
            self.listbox_ship = Listbox(self.ship_select_canvas, width=198
                                        , background=app.confalternate_left_nav_background, borderwidth=1)
            for ship in self.player.ships:
                self.listbox_ship.insert(END, ship.name)
            self.listbox_ship.grid(row=row, columnspan=4, sticky='w,e')
            self.listbox_ship.bind('<<ListboxSelect>>', self.poll_ship_list)
            row += 1
            self.label_ship_name = Label(self.ship_select_canvas, text="No Ship Selected", fg=app.confsecond_text_color)
            self.label_ship_name.config(background=app.confleft_nav_background)
            self.label_ship_name.grid(row=row, columnspan=4, sticky='w')

            row += 1
            self.label_separator_s = Label(self.ship_select_canvas, text="", fg=app.confleft_nav_background, width=24)
            self.label_separator_s.config(background=app.confleft_nav_background)
            self.label_separator_s.grid(row=row, columnspan=4, sticky='e,w')

        if app.confdebug == 1:
            print "CreatedLine:", 0, " ", 0, " ", main_window.sw-200, " ", main_window.sh-200
            print "CreatedLine:", main_window.sw-200, " ", 0, " ", 0, " ", main_window.sh-200
            print "CurrWin0:", convert_coords_x(main_window, 0), convert_coords_y(main_window, 0)

        if app.confdebug == 1:
            print "Displayed: left_nav,", main_window.sh, ",200"

    def poll_ship_list(self, event):

        w = event.widget
        index = int(w.curselection()[0])
        new_ship_name = w.get(index)
        if isset(self.selected_ship_name):
            if self.selected_ship_name == "":
                if new_ship_name != self.selected_ship_name:
                    self.ship_selction_has_changed(new_ship_name)
                    self.selected_ship_name = new_ship_name
                    self.selected_ship_id = w.curselection()
                    if app.confdebug == 1:
                        print "SelectedShip:", self.selected_ship_name
                    self.redraw(self.main_window, self.player)
        else:
            self.selected_ship_name = new_ship_name
            self.selected_ship_id = w.curselection()
            if app.confdebug == 1:
                print "SelectedShip:", self.selected_ship_name
            self.redraw(self.main_window, self.player)

    def redraw(self, main_window, player):

        app = self.app
        main_window = app.main_controller.view
        player = app.game.player

        self.player = player

        if app.confdebug == 1:
            print "Redrawing Left Nav"

        self.label_logo.place(anchor='n', x=100, y=0)
        self.resources_canvas.config(background=app.confleft_nav_background,
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

        if app.confdebug == 1:
            print "Left Buttons Start Y:", self.left_buttons_start_y

        # Planet Info Set

        row = 0
        self.planet_info_start_y = self.resources_start_y + 115
        self.planet_info_canvas.place(anchor='nw', x=0, y=self.planet_info_start_y)
        self.label_planet_info.grid(row=row, column=0, sticky='w')
        row += 1
        self.label_planet_name.grid(row=row, column=0, sticky='w')
        self.label_planet_name_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_planet_metals.grid(row=row, column=0, sticky='w')
        self.label_planet_metals_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_planet_food.grid(row=row, column=0, sticky='w')
        self.label_planet_food_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_planet_terrain.grid(row=row, column=0, sticky='w')
        self.label_planet_terrain_val.grid(row=row, column=1, sticky='e')
        row += 1
        self.label_separator_p.grid(row=row, columnspan=2, sticky='e,w')

        # prep for ship section

        if isset(self.ship_select_canvas):
            self.ship_select_canvas.destroy()

        # ship info

        row = 0
        self.ship_select_start_y = self.planet_info_start_y + 115
        self.ship_select_canvas = Canvas(self.left_canvas)
        self.ship_select_canvas.config(background=app.confleft_nav_background,
                                       width=198,
                                       highlightthickness=0,
                                       border=0)
        self.ship_select_canvas.grid_propagate(False)
        self.ship_select_canvas.place(anchor='nw', x=0, y=self.ship_select_start_y)
        self.label_ship_select = Label(self.ship_select_canvas, text="Select Ship:", fg=app.confmain_text_color)
        self.label_ship_select.config(background=app.confleft_nav_background)
        self.label_ship_select.grid(row=row, column=0, sticky='w')

        # future implementation

        # if selected_ship.name != '':
        if self.selected_ship_name != "":

            if app.confdebug == 1:
                print "Showing Selected Ship (redraw)"

            current_ship = self.player.get_ship(self.selected_ship_name)

            row += 1
            self.listbox_ship = Listbox(self.ship_select_canvas, width=198
                                        , background=app.confalternate_left_nav_background, borderwidth=1)
            self.listbox_ship.config(selectmode=SINGLE)
            for ship in self.player.ships:
                self.listbox_ship.insert(END, ship.name)
            self.listbox_ship.selection_set(self.selected_ship_id)
            self.listbox_ship.grid(row=row, columnspan=4, sticky='w,e')
            self.listbox_ship.bind('<<ListboxSelect>>', self.poll_ship_list)

            row = 0
            self.ship_info_start_y = self.ship_select_start_y + 200
            self.ship_info_canvas = Canvas(self.left_canvas)
            self.ship_info_canvas.config(background=app.confleft_nav_background,
                                         width=198,
                                         highlightthickness=0,
                                         border=0)
            self.ship_info_canvas.grid_propagate(False)
            self.ship_info_canvas.place(anchor='nw', x=0, y=self.ship_info_start_y)
            self.label_ship_info = Label(self.ship_info_canvas, text="Ship Info:", fg=app.confmain_text_color)
            self.label_ship_info.config(background=app.confleft_nav_background)
            self.label_ship_info.grid(row=row, column=0, sticky='w')

            row += 1
            self.label_ship_name = Label(self.ship_info_canvas, text="Name:", fg=app.confsecond_text_color)
            self.label_ship_name.config(background=app.confleft_nav_background)
            self.label_ship_name.grid(row=row, column=0, columnspan=2, sticky='w')
            self.label_ship_name_val = Label(self.ship_info_canvas, text=current_ship.name
                                             , fg=app.confsecond_text_color)
            self.label_ship_name_val.config(background=app.confleft_nav_background)
            self.label_ship_name_val.grid(row=row, column=2, columnspan=2, sticky='e')

            row += 1
            self.label_ship_attack = Label(self.ship_info_canvas, text="Attack:", fg=app.confsecond_text_color)
            self.label_ship_attack.config(background=app.confleft_nav_background)
            self.label_ship_attack.grid(row=row, column=0, sticky='w')
            self.label_ship_attack_val = Label(self.ship_info_canvas, text=current_ship.attack
                                             , fg=app.confsecond_text_color)
            self.label_ship_attack_val.config(background=app.confleft_nav_background)
            self.label_ship_attack_val.grid(row=row, column=1, sticky='e')
            self.label_ship_defense = Label(self.ship_info_canvas, text="Defense:", fg=app.confsecond_text_color)
            self.label_ship_defense.config(background=app.confleft_nav_background)
            self.label_ship_defense.grid(row=row, column=2, sticky='w')
            self.label_ship_defense_val = Label(self.ship_info_canvas, text=current_ship.defense
                                             , fg=app.confsecond_text_color)
            self.label_ship_defense_val.config(background=app.confleft_nav_background)
            self.label_ship_defense_val.grid(row=row, column=3, sticky='e')

            row += 1
            self.label_ship_storage = Label(self.ship_info_canvas, text="Storage:", fg=app.confsecond_text_color)
            self.label_ship_storage.config(background=app.confleft_nav_background)
            self.label_ship_storage.grid(row=row, column=0, columnspan=2, sticky='w')
            self.label_ship_storage_val = Label(self.ship_info_canvas, text=current_ship.storage
                                             , fg=app.confsecond_text_color)
            self.label_ship_storage_val.config(background=app.confleft_nav_background)
            self.label_ship_storage_val.grid(row=row, column=2, columnspan=2, sticky='e')

            row += 1
            self.label_ship_seats = Label(self.ship_info_canvas, text="Seats:", fg=app.confsecond_text_color)
            self.label_ship_seats.config(background=app.confleft_nav_background)
            self.label_ship_seats.grid(row=row, column=0, columnspan=2, sticky='w')
            self.label_ship_seats_val = Label(self.ship_info_canvas, text=current_ship.seats
                                             , fg=app.confsecond_text_color)
            self.label_ship_seats_val.config(background=app.confleft_nav_background)
            self.label_ship_seats_val.grid(row=row, column=2, columnspan=2, sticky='e')

            row += 1
            self.label_separator_s = Label(self.ship_info_canvas, text="", fg=app.confleft_nav_background, width=24)
            self.label_separator_s.config(background=app.confleft_nav_background)
            self.label_separator_s.grid(row=row, columnspan=4, sticky='e,w')

        else:

            if app.confdebug == 1:
                print "No Selected Ship Detected (redraw)"

            row += 1
            self.listbox_ship = Listbox(self.ship_select_canvas, width=198
                                        , background=app.confalternate_left_nav_background, borderwidth=1)
            for ship in self.player.ships:
                self.listbox_ship.insert(END, ship.name)
            self.listbox_ship.grid(row=row, columnspan=2, sticky='w,e')
            self.listbox_ship.bind('<<ListboxSelect>>', self.poll_ship_list)
            row += 1
            self.label_ship_name = Label(self.ship_select_canvas, text="No Ship Selected", fg=app.confsecond_text_color)
            self.label_ship_name.config(background=app.confleft_nav_background)
            self.label_ship_name.grid(row=row, columnspan=2, sticky='w')

            row += 1
            self.label_separator_s = Label(self.ship_select_canvas, text="", fg=app.confleft_nav_background, width=24)
            self.label_separator_s.config(background=app.confleft_nav_background)
            self.label_separator_s.grid(row=row, columnspan=4, sticky='e,w')





def convert_coords_x(main_window, x):
    return ((main_window.sw - 200) / 2) + x


def convert_coords_y(main_window, y):
    return ((main_window.sh - 200) / 2) + y


def convert_coords_name(main_window, y, size):
    return ((main_window.sh - 200) / 2) + y - (size / 2) - app.confplanet_name_height

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
