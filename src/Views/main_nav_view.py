from Tkinter import Frame, Label, Canvas, CENTER
from PIL import Image, ImageTk
from math import atan2, pi, cos, sin, hypot


class MainNavView(Frame):
    def __init__(self, controller, parent):
        self.controller = controller
        self.parent = parent
        self.app = self.controller.app
        self.enabled = False
        self.has_selected = False
        self.planet_images = []

        self.main_window = controller.parent.view
        self.main_nav = Frame(self.main_window, height=self.main_window.sh, width=self.main_window.sw - 200, background='black')
        # self.main_nav = Frame.__init__(self.main_window, height=self.main_window.sh, width=self.main_window.sw - 200, background='black')

        self.main_nav.place(x=200, y=0)
        self.main_canvas = Canvas(self.parent)
        self.main_canvas_has_been_created = True

    def build(self):  # formerly build_main_nav

        self.app.debug("Building Main Nav View")

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

        self.app.debug(("Displayed: main_nav,", main_window.sw - 200, ",", main_window.sh))

        # draw corner lines
        if self.app.conf.debug_lines == 1:
            self.main_canvas.create_line(0, 0, main_window.sw - 200, main_window.sh, fill='red')
            self.main_canvas.create_line(main_window.sw - 200, 0, 0, main_window.sh, fill='red')

        if self.app.conf.debug == 1:
            print "CreatedLine:", 0, " ", 0, " ", main_window.sw - 200, " ", main_window.sh
            print "CreatedLine:", main_window.sw - 200, " ", 0, " ", 0, " ", main_window.sh
            print "CurrWin0:", self.convert_coordinates_x(0), self.convert_coordinates_y(0)

        self.main_canvas.config(width=main_window.sw - 200, height=main_window.sh)
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

        app = self.app
        main_window = app.main_controller.view

        if self.main_canvas_has_been_created:
            self.main_canvas.config(width=main_window.sw - 200, height=main_window.sh)
            self.main_canvas.delete('all')
            self.finish_drawing_planets()
            self.app.debug("Redraw:AlreadyCreated")
        else:
            self.build_planet_view()
            self.app.debug("Redraw:New")

    def finish_drawing_planets(self):

        self.main_canvas.pack(fill='both')
        main_window = self.controller.parent.view
        self.app.debug(("WindowSize:", main_window.sw, ":", main_window.sh))

    def draw_planet(self, planet):

        # global main_nav, main_canvas, label, planet_images, main_window

        new_x = self.convert_coordinates_x(planet.loc.x)
        new_y = self.convert_coordinates_y(planet.loc.y)
        name_y = self.convert_coordinates_name(planet.loc.y, planet.loc.size)
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
        label.planet_image_res = planet_image_res  # keep a reference!
        label.place(anchor=CENTER, x=new_x, y=new_y)
        label.bind("<Button-1>", lambda event, arg=planet: self.controller.select_planet(event, arg))

        label_name = Label(self.main_canvas, text=planet.name, fg=self.app.conf.main_text_color, bg='black'
                           , borderwidth=1
                           , highlightthickness=0)
        label_name.place(anchor=CENTER, x=new_x, y=name_y)

        if self.app.conf.debug == 1:
            print "Drawing planet: [", planet.name, ",", new_x, ",", new_y, ",", planet.loc.size, ",", color, "]"

    def draw_planet_highlighted(self, planet):

        # global main_nav, main_canvas, label, planet_images, main_window

        new_x = self.convert_coordinates_x(planet.loc.x)
        new_y = self.convert_coordinates_y(planet.loc.y)
        name_y = self.convert_coordinates_name(planet.loc.y, planet.loc.size)
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
        label_planet.planet_image_res = planet_image_res  # keep a reference!
        label_planet.place(anchor=CENTER, x=new_x, y=new_y)
        label_planet.bind("<Button-1>", lambda event, arg=planet: self.controller.select_planet(event, arg))
        label_name = Label(self.main_canvas, text=planet.name, fg='red', bg='black', borderwidth=1
                           , highlightthickness=0)
        label_name.place(anchor=CENTER, x=new_x, y=name_y)

        if self.app.conf.debug == 1:
            print "Drawing planet: [", planet.name, ",", new_x, ",", new_y, ",", planet.loc.size, ",", color, "]"

        # get nearest planet and draw a line
        if self.has_selected:
            nearest_planet = self.get_nearest_planet(planet)
            l = self.get_line_points((planet.loc.x, planet.loc.y)
                                     , (nearest_planet.loc.x, nearest_planet.loc.y)
                                     , planet.loc.size
                                     , nearest_planet.loc.size)
            self.main_canvas.create_line(l.x1, l.y1, l.x2, l.y2, fill='blue', dash=(4, 4))
            self.main_canvas.pack()
            self.app.debug(("Drawing line:", l.x1, ',', l.y1, ',', l.x2, ',', l.y2))
        else:
            self.app.debug("Line next time")
            self.has_selected = True

    def draw_planet_h(self, planet):

        # global main_nav, main_canvas, label, planet_images, main_window

        new_x = self.convert_coordinates_x(planet.loc.x)
        new_y = self.convert_coordinates_y(planet.loc.y)
        name_y = self.convert_coordinates_name(planet.loc.y, planet.loc.size)
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
        label_planet.planet_image_res = planet_image_res  # keep a reference!
        label_planet.place(anchor=CENTER, x=new_x, y=new_y)
        label_planet.bind("<Button-1>", lambda event, arg=planet: self.controller.select_planet(event, arg))
        label_name = Label(self.main_canvas, text=planet.name, fg='red', bg='black', borderwidth=1
                           , highlightthickness=0)
        label_name.place(anchor=CENTER, x=new_x, y=name_y)

        if self.app.conf.debug == 1:
            print "Drawing planet: [", planet.name, ",", new_x, ",", new_y, ",", planet.loc.size, ",", color, "]"

    def get_nearest_planet(self, planet):
        planets = self.app.game.player.planets
        distances = {}
        for i in range(len(planets)):
            if planets[i].name != planet.name:
                print i
                tmp = self.get_distance(planet, planets[i])
                distances[i] = tmp
        self.app.debug(("Found nearest planet:", planets[min(distances)].name, "and", planet.name))
        self.draw_planet_h(planets[min(distances)])
        return planets[min(distances)]

    @staticmethod
    def get_distance(planet1, planet2):
        return hypot(planet2.loc.x - planet1.loc.x, planet2.loc.y - planet1.loc.y)

    def redraw_planet(self, planet):

        self.draw_planet(self.app.game.player.last_selected_planet)
        self.draw_planet_highlighted(planet)

    @staticmethod
    def get_terrain_color(terrain):

        """

        :param terrain:
        :return:

        # Planet Terrains
        # 1 Ice
        # 2 Rock
        # 3 Green
        # 4 Water
        # 5 Alien

        """

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

    def convert_coordinates_x(self, x):
        main_window = self.app.main_controller.view
        return ((main_window.sw - 200) / 2) + x

    def convert_coordinates_y(self, y):
        main_window = self.app.main_controller.view
        return (main_window.sh / 2) + y

    def convert_coordinates_name(self, y, size):
        main_window = self.app.main_controller.view
        return (main_window.sh / 2) + y - (size / 2) - self.app.conf.planet_name_height

    @staticmethod
    def angle(pt1, pt2):
        x1, y1 = pt1
        x2, y2 = pt2

        deltax = x2 - x1
        deltay = y2 - y1

        angle_rad = atan2(deltay, deltax)
        angle_deg = angle_rad * 180.0 / pi

        # return angle_rad
        return angle_deg

    def get_line_points(self, p1, p2, p1width, p2width):

        # initialize vars

        x1, y1 = p1
        x2, y2 = p2

        self.app.debug(("x1", x1))
        self.app.debug(("y1", y1))
        self.app.debug(("x2", x2))
        self.app.debug(("y2", y2))

        # x3 = 0
        # y3 = 0
        # x4 = 0
        # y4 = 0

        # get angle1

        a1 = self.angle(p1, p2)

        # determine line start distance from planet centers

        o1 = 2 * p1width
        o2 = 2 * p2width

        # get first point of the line

        x3 = x1 + (cos(a1) * o1)
        y3 = y1 + (sin(a1) * o1)

        # get angle 2

        a2 = (90 + a1) - 180

        # establish 2nd point of the line

        x4 = x2 + (cos(a2) * o2)
        y4 = y2 + (sin(a2) * o2)

        # convert coordinates for window size

        x3 = self.convert_coordinates_x(x3)
        y3 = self.convert_coordinates_y(y3)
        x4 = self.convert_coordinates_x(x4)
        y4 = self.convert_coordinates_y(y4)

        # create object to return

        line_points = LinePoints(x3, y3, x4, y4)

        return line_points

    def get_line_points_(self, p1, p2, p1width, p2width):

        # initialize vars

        x1, y1 = p1
        x2, y2 = p2

        # x3 = 0
        # y3 = 0
        # x4 = 0
        # y4 = 0

        # get angle1

        a1 = self.angle(p1, p2)

        # determine line start distance from planet centers

        o1 = 2 * p1width
        o2 = 2 * p2width

        # get first point of the line

        x3 = x1 + (cos(a1) * o1)
        y3 = y1 + (sin(a1) * o1)

        # get angle 2

        a2 = (90 + a1) - 180

        # establish 2nd point of the line

        x4 = x2 + (cos(a2) * o2)
        y4 = y2 + (sin(a2) * o2)

        # create object to return

        line_points = LinePoints(x3, y3, x4, y4)

        return line_points


# class used to return values from get_line_points method


class LinePoints(object):
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2