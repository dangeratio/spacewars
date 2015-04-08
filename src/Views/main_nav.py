


class MainNav(object):
    def __init__(self):
        pass

    def build(self):        # formerly build_main_nav

        global left_nav, bottom_nav, main_nav, map_nav, navs_have_been_built, main_window

        left_nav = Frame(main_window, height=main_window.sh, width=200, background=conf.left_nav_background)
        bottom_nav = Frame(main_window, height=200, width=(main_window.sw-200), background=conf.bottom_nav_background)
        main_nav = Frame(main_window, height=main_window.sh, width=main_window.sw-200, background='black')
        map_nav = Frame(main_window, height=200, width=200, background=conf.left_nav_background)

        # build_bottom_nav_menu()
        # build_map()

        if navs_have_been_built:
            if conf.debug == 1:
                print "Redrawing..."
            left.redraw(main_window, player)
            # redraw_planet_view()
            main_canvas.destroy()
            build_planet_view()
        else:
            if conf.debug == 1:
                print "Drawing..."
            build_planet_view()
            build_left_nav_menu()
            navs_have_been_built = True


    def build_planet_view(self):

        global main_canvas_has_been_created, main_nav, main_canvas

        if conf.debug == 1:
            print "Displayed: main_nav,", main_window.sw-200, ",", main_window.sh

        main_nav.place(x=200, y=0)
        main_canvas = Canvas(main_nav)
        main_canvas_has_been_created = True

        # draw corner lines
        if conf.debug_lines == 1:
            main_canvas.create_line(0, 0, main_window.sw-200, main_window.sh, fill='red')
            main_canvas.create_line(main_window.sw-200, 0, 0, main_window.sh, fill='red')

        if conf.debug == 1:
            print "CreatedLine:", 0, " ", 0, " ", main_window.sw-200, " ", main_window.sh
            print "CreatedLine:", main_window.sw-200, " ", 0, " ", 0, " ", main_window.sh
            print "CurrWin0:", convert_coords_x(0), convert_coords_y(0)

        main_canvas.config(width=main_window.sw-200, height=main_window.sh)
        main_canvas.config(background='black')
        main_canvas.config(highlightbackground=conf.main_background)
        main_canvas.config(highlightthickness=0)

        if conf.debug == 1:
            print "*********************"
            print "***Drawing Planets***"
            print "*********************"

        # draw planets
        for planet in player.planets:
            if conf.debug == 1:
                print "init:", planet.loc.x, ",", planet.loc.y
            if planet == player.selected_planet:
                draw_planet_highlighted(planet)
            else:
                draw_planet(planet)

        finish_drawing_planets()


    def redraw_planet_view(self):

        global main_window, main_canvas

        if main_canvas_has_been_created:

            global main_canvas
            main_canvas.config(width=main_window.sw-200, height=main_window.sh)
            main_canvas.delete('all')
            finish_drawing_planets()
            if conf.debug == 1:
                print "Redraw:AlreadyCreated"

        else:

            build_planet_view()
            if conf.debug == 1:
                print "Redraw:New"


    def finish_drawing_planets(self):

        global main_canvas, main_window

        main_canvas.pack(fill='both')
        if conf.debug == 1:
            # print "Drawing: NewLoc:", player.new_loc
            # print "Drawing: Failed:", player.failed_to_find
            print "WindowSize:", main_window.sw, ":", main_window.sh
            # print "PlanetsDrawn:", len(player.planets)


    def draw_planet(self, planet):

        global main_nav, main_canvas, label, planet_images, main_window

        new_x = convert_coords_x(planet.loc.x)
        new_y = convert_coords_y(planet.loc.y)
        name_y = convert_coords_name(planet.loc.y, planet.loc.size)
        color = get_terrain_color(planet.terrain)

        size = planet.loc.size, planet.loc.size
        planet_image = Image.open(get_terrain_image(planet.terrain))
        planet_image.thumbnail(size, Image.ANTIALIAS)
        planet_image_res = ImageTk.PhotoImage(planet_image)
        new_planet_image = planet_image_res
        planet_images.append(new_planet_image)
        label = Label(main_canvas)
        label.config(image=planet_image_res)
        label.config(background='black')
        label.grid()
        label.planet_image_res = planet_image_res           # keep a reference!
        label.place(anchor=CENTER, x=new_x, y=new_y)
        label.bind("<Button-1>", lambda event, arg=planet: select_planet(event, arg))

        label_name = Label(main_canvas, text=planet.name, fg=conf.main_text_color, bg='black', borderwidth=1
                           , highlightthickness=0)
        label_name.place(anchor=CENTER, x=new_x, y=name_y)

        if conf.debug == 1:
            print "Drawing planet: [", planet.name, ",", new_x, ",", new_y, ",", planet.loc.size, ",", color, "]"


    def draw_planet_highlighted(self, planet):

        global main_nav, main_canvas, label, planet_images, main_window

        new_x = convert_coords_x(planet.loc.x)
        new_y = convert_coords_y(planet.loc.y)
        name_y = convert_coords_name(planet.loc.y, planet.loc.size)
        color = get_terrain_color(planet.terrain)

        size = planet.loc.size, planet.loc.size
        planet_image = Image.open(get_terrain_image(planet.terrain))
        planet_image.thumbnail(size, Image.ANTIALIAS)
        planet_image_res = ImageTk.PhotoImage(planet_image)
        new_planet_image = planet_image_res
        planet_images.append(new_planet_image)
        label_planet = Label(main_canvas)
        label_planet.config(image=planet_image_res)
        label_planet.config(background='black')
        label_planet.planet_image_res = planet_image_res           # keep a reference!
        label_planet.place(anchor=CENTER, x=new_x, y=new_y)
        label_planet.bind("<Button-1>", lambda event, arg=planet: select_planet(event, arg))
        label_name = Label(main_canvas, text=planet.name, fg='red', bg='black', borderwidth=1
                           , highlightthickness=0)
        label_name.place(anchor=CENTER, x=new_x, y=name_y)


        if conf.debug == 1:
            print "Drawing planet: [", planet.name, ",", new_x, ",", new_y, ",", planet.loc.size, ",", color, "]"






def get_terrain_color(terrain):

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


def get_terrain_image(terrain):

    # Planet Terrains
    # 1 Ice
    # 2 Rock
    # 3 Green
    # 4 Water
    # 5 Alien

    if terrain == 1:
        return conf.ice_planet_image_path
    elif terrain == 2:
        return conf.rock_planet_image_path
    elif terrain == 3:
        return conf.green_planet_image_path
    elif terrain == 4:
        return conf.water_planet_image_path
    elif terrain == 5:
        return conf.alien_planet_image_path
    else:
        return conf.alien_planet_image_path


def convert_coords_x(x):
    return ((main_window.sw - 200) / 2) + x


def convert_coords_y(y):
    return (main_window.sh / 2) + y


def convert_coords_name(y, size):
    global main_window
    return (main_window.sh / 2) + y - (size / 2) - conf.planet_name_height

