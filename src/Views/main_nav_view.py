from Tkinter import Frame, Label, Canvas, CENTER
from PIL import Image, ImageTk


class MainNavView(Frame):
    def __init__(self, controller, parent):
        self.controller = controller
        self.parent = parent
        self.app = self.controller.app
        self.enabled = False
        self.planet_images = []

    def build(self):        # formerly build_main_nav

        self.app.debug("Building Main Nav View")

        main_window = self.app.main_controller.view
        self.main_nav = Frame(main_window, height=main_window.sh, width=main_window.sw-200, background='black')

        if self.enabled:
            self.main_canvas.destroy()
            self.build_planet_view()
        else:
            self.build_planet_view()
            self.enabled = True


    def build_planet_view(self):

        app = self.app
        main_window = app.main_controller.view
        player = app.game.player

        # global main_canvas_has_been_created, main_nav, main_canvas

        self.app.debug(("Displayed: main_nav,", main_window.sw-200, ",", main_window.sh))

        self.main_nav.place(x=200, y=0)
        self.main_canvas = Canvas(self.main_nav)
        self.main_canvas_has_been_created = True

        # draw corner lines
        if self.app.conf.debug_lines == 1:
            self.main_canvas.create_line(0, 0, main_window.sw-200, main_window.sh, fill='red')
            self.main_canvas.create_line(main_window.sw-200, 0, 0, main_window.sh, fill='red')

        if self.app.conf.debug == 1:
            print "CreatedLine:", 0, " ", 0, " ", main_window.sw-200, " ", main_window.sh
            print "CreatedLine:", main_window.sw-200, " ", 0, " ", 0, " ", main_window.sh
            print "CurrWin0:", self.convert_coords_x(0), self.convert_coords_y(0)

        self.main_canvas.config(width=main_window.sw-200, height=main_window.sh)
        self.main_canvas.config(background='black')
        self.main_canvas.config(highlightbackground=self.app.conf.main_background)
        self.main_canvas.config(highlightthickness=0)

        if self.app.conf.debug == 1:
            print "*********************"
            print "***Drawing Planets***"
            print "*********************"

        # draw planets
        for planet in player.planets:
            if self.app.conf.debug == 1:
                print "init:", planet.loc.x, ",", planet.loc.y
            if planet == player.selected_planet:
                self.draw_planet_highlighted(planet)
            else:
                self.draw_planet(planet)

        self.finish_drawing_planets()

    def redraw_planet_view(self):

        # global main_window, main_canvas

        if self.main_canvas_has_been_created:
            self.main_canvas.config(width=main_window.sw-200, height=main_window.sh)
            self.main_canvas.delete('all')
            self.finish_drawing_planets()
            self.app.debug("Redraw:AlreadyCreated")
        else:
            self.build_planet_view()
            self.app.debug("Redraw:New")

    def finish_drawing_planets(self):

        # global main_canvas, main_window

        self.main_canvas.pack(fill='both')
        main_window = self.controller.parent.view
        if self.app.conf.debug == 1:
            # print "Drawing: NewLoc:", player.new_loc
            # print "Drawing: Failed:", player.failed_to_find
            print "WindowSize:", main_window.sw, ":", main_window.sh
            # print "PlanetsDrawn:", len(player.planets)


    def draw_planet(self, planet):

        # global main_nav, main_canvas, label, planet_images, main_window

        new_x = self.convert_coords_x(planet.loc.x)
        new_y = self.convert_coords_y(planet.loc.y)
        name_y = self.convert_coords_name(planet.loc.y, planet.loc.size)
        color = self.get_terrain_color(planet.terrain)

        size = planet.loc.size, planet.loc.size
        planet_image = Image.open(self.get_terrain_image(planet.terrain))
        planet_image.thumbnail(size, Image.ANTIALIAS)
        planet_image_res = ImageTk.PhotoImage(planet_image)
        new_planet_image = planet_image_res
        self.planet_images.append(new_planet_image)
        label = Label(self.main_canvas)
        label.config(image=planet_image_res)
        label.config(background='black')
        label.grid()
        label.planet_image_res = planet_image_res           # keep a reference!
        label.place(anchor=CENTER, x=new_x, y=new_y)
        label.bind("<Button-1>", lambda event, arg=planet: self.select_planet(event, arg))

        label_name = Label(self.main_canvas, text=planet.name, fg=self.app.conf.main_text_color, bg='black'
                           , borderwidth=1
                           , highlightthickness=0)
        label_name.place(anchor=CENTER, x=new_x, y=name_y)

        if self.app.conf.debug == 1:
            print "Drawing planet: [", planet.name, ",", new_x, ",", new_y, ",", planet.loc.size, ",", color, "]"


    def draw_planet_highlighted(self, planet):

        # global main_nav, main_canvas, label, planet_images, main_window

        new_x = self.convert_coords_x(planet.loc.x)
        new_y = self.convert_coords_y(planet.loc.y)
        name_y = self.convert_coords_name(planet.loc.y, planet.loc.size)
        color = self.get_terrain_color(planet.terrain)

        size = planet.loc.size, planet.loc.size
        planet_image = Image.open(self.get_terrain_image(planet.terrain))
        planet_image.thumbnail(size, Image.ANTIALIAS)
        planet_image_res = ImageTk.PhotoImage(planet_image)
        new_planet_image = planet_image_res
        self.planet_images.append(new_planet_image)
        label_planet = Label(self.main_canvas)
        label_planet.config(image=planet_image_res)
        label_planet.config(background='black')
        label_planet.planet_image_res = planet_image_res           # keep a reference!
        label_planet.place(anchor=CENTER, x=new_x, y=new_y)
        label_planet.bind("<Button-1>", lambda event, arg=planet: self.controller.select_planet(event, arg))
        label_name = Label(self.main_canvas, text=planet.name, fg='red', bg='black', borderwidth=1
                           , highlightthickness=0)
        label_name.place(anchor=CENTER, x=new_x, y=name_y)

        if self.app.conf.debug == 1:
            print "Drawing planet: [", planet.name, ",", new_x, ",", new_y, ",", planet.loc.size, ",", color, "]"

    def get_terrain_color(self, terrain):

        # Planet Terrains
        # 1 Ice
        # 2 Rock
        # 3 Green
        # 4 Water
        # 5 Alien

        if terrain == 1:
            return 'ice'
        elif terrain == 2:
            return 'rock'
        elif terrain == 3:
            return 'green'
        elif terrain == 4:
            return 'water'
        elif terrain == 5:
            return 'alien'
        else:
            return 'black'


    def get_terrain_image(self, terrain):

        # Planet Terrains
        # 1 Ice
        # 2 Rock
        # 3 Green
        # 4 Water
        # 5 Alien

        if terrain == 1:
            return self.app.conf.ice_planet_image_path
        elif terrain == 2:
            return self.app.conf.rock_planet_image_path
        elif terrain == 3:
            return self.app.conf.green_planet_image_path
        elif terrain == 4:
            return self.app.conf.water_planet_image_path
        elif terrain == 5:
            return self.app.conf.alien_planet_image_path
        else:
            return self.app.conf.alien_planet_image_path


    def convert_coords_x(self, x):
        main_window = self.app.main_controller.view
        return ((main_window.sw - 200) / 2) + x


    def convert_coords_y(self, y):
        main_window = self.app.main_controller.view
        return (main_window.sh / 2) + y


    def convert_coords_name(self, y, size):
        main_window = self.app.main_controller.view
        return (main_window.sh / 2) + y - (size / 2) - self.app.conf.planet_name_height

