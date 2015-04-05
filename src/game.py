from Tkinter import Tk, Frame, Label, Button, Canvas, CENTER
from PIL import Image, ImageTk, ImageDraw
from math import sqrt

from ship import *
from planet import *
from player import *
from configfile import *
from left_nav import *

# load config file
conf = ConfigFile()
conf.print_debug()


# colors and intro
'''
_conf.window_background = "#071722"
__conf.window_background = "#162026"
___conf.window_background = "#5B585A"
conf.window_background = "black"
conf.main_background = "#5B585A"
conf.black_color = "#000000"
conf.left_nav_background = "#5E677A"
_conf.intro_background = "#5E677A"
conf.intro_background = "#5B585A"
conf.bottom_nav_background = "#93AEA6"
'''
conf.title_image_path = "../img/title_image.jpg"
intro_padding_height = 77.5
navs_have_been_built = False

# initial generation variables
selected_planet = ""
selected_ship = ""

# planet images
ice_planet_image_path = "../img/ice_planet.gif"
rock_planet_image_path = "../img/rock_planet.gif"
green_planet_image_path = "../img/green_planet.gif"
water_planet_image_path = "../img/water_planet.gif"
alien_planet_image_path = "../img/alien_planet.gif"
planet_images = []

# error counters

'''
active_view variable controls what view is displayed.  These are the values:
- intro: this is the first screen a user sees when they enter the game
- main: this is the main game screen the user will spend most of the time in the game playing
'''
active_view = "intro"


class MainWindow(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background=conf.window_background)

        self.parent = parent

        self.parent.title("space")
        # Handle click event
        # self.bind("<Button-1>", click)
        self.bind("<Configure>", resize)
        self.pack(fill='both', expand=1)

        self.sw = self.winfo_screenwidth()
        self.sh = self.winfo_screenheight()

        self.update()

        '''
        # Test Code
        print self.winfo_height()
        print self.winfo_reqheight()
        print self.winfo_screenheight()
        print self.winfo_vrootheight()
        print ""
        print self.winfo_screenwidth()
        print self.winfo_vrootwidth()
        '''

        self.parent.geometry('%dx%d+%d+%d' % (self.sw, self.sh, 0, 0))

    def remove_this(self):
        self.frame.destroy()


class ContainerFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background=conf.window_background)
        self.parent = parent
        self.update()

    def remove_this(self):
        self.frame.destroy()


#
# general window handling
#


def click(event):
    print "clicked at", event.x, event.y


def resize(event):
    # Debug
    # print "resize to", event.width, event.height

    global main_window, active_view

    main_window.sw = event.width
    main_window.sh = event.height

    if main_window.sw <= 500:
        main_window.sw = 500

    if main_window.sh <= 500:
        main_window.sh = 500

    if conf.debug == 1:
        print "(", main_window.sw, ",", main_window.sh, ",", active_view, ")"

    if active_view == "intro":
        draw_intro_nav()
    elif active_view == "main":
        build_main_nav()


def main():
    # build_variables()
    init_intro_nav()
    draw_intro_nav()
    # build_menus()
    root.mainloop()

'''
def build_variables():
    user_ship = Ship(1, 1, 1, 1, 1)
    user_planet_location = Location(10, 10, 1)
    user_planet = InitialPlanet()
    user = Player("joe", [user_planet], 1, 1, 1)
'''

#
# introduction handling
#


def hide_intro_nav():
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


def init_intro_nav():
    global intro_nav, background_frame, can, button_load_game\
        , button_new_game, button_quit, intro_fill_bottom\
        , label_version, title_image_res\
        , intro_top_padding, intro_btm_padding

    # frame setup

    background_frame = Frame(main_window, height=main_window.sh, width=main_window.sw, background=conf.window_background)
    intro_nav = Frame(background_frame, height=500, width=500, background=conf.intro_background)

    # elements

    intro_top_padding = Canvas(intro_nav)
    intro_top_padding.configure(height=intro_padding_height, background=conf.intro_background, highlightbackground=conf.intro_background)

    title_image_resource = Image.open(conf.title_image_path)
    title_image_res = ImageTk.PhotoImage(title_image_resource)
    can = Canvas(intro_nav, background=conf.intro_background, highlightbackground=conf.intro_background)
    can.title_image_res = title_image_res
    can.config(width=title_image_res.width(), height=title_image_res.height())

    button_new_game = Button(intro_nav, text="New Game", command=event_button_new_game, bg=conf.intro_background)
    button_new_game.config(highlightbackground=conf.intro_background)

    button_load_game = Button(intro_nav, text="Load Game", command=event_button_load_game, bg=conf.intro_background)
    button_load_game.config(highlightbackground=conf.intro_background)
    button_load_game.config(state='disabled')

    button_quit = Button(intro_nav, text="Quit", command=event_button_quit, bg=conf.intro_background)
    button_quit.config(highlightbackground=conf.intro_background)

    label_version = Label(intro_nav, bg=conf.intro_background, text=conf.version)

    intro_btm_padding = Canvas(intro_nav)
    intro_btm_padding.configure(height=intro_padding_height, background=conf.intro_background, highlightbackground=conf.intro_background)


def draw_intro_nav():

    # frame setup

    if conf.debug == 1:
        pass
        # canvas = Canvas(background_frame)
        # canvas.create_line((0, 0, main_window.sw, main_window.sh), fill=conf.black_color)
        # canvas.pack()

    intro_top_padding.pack()

    background_frame.pack(fill='both')
    intro_nav.pack(fill='both', padx=(main_window.sw/2)-250, pady=(main_window.sh/2)-250)

    if conf.debug == 1:
        print "Drew Intro, padding: (", (main_window.sw/2)-250, ",", (main_window.sh/2)-250, ")"

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
    # button_new_game.invoke()


def quitting():
    # do any needed cleanup
    exit()


def event_button_new_game():
    initiate_new_game()


def event_button_load_game():
    pass
    # not yet implemented


def event_button_quit():
    quitting()


# main game handling


class Game(object):
    def __init__(self, player):
        self.player = player


def initiate_new_game():

    global active_view

    hide_intro_nav()
    active_view = "main"

    global player, selected_planet, game

    initial_planet = InitialPlanet()
    initial_ship = InitialShip(initial_planet)
    player = InitialPlayer(initial_planet, initial_ship)
    for i in range(conf.planets_to_generate):
        player.generate_new_planet()
        # new_planet = GeneratePlanet(conf.max_distance)
        # player.planets.append(new_planet)
    game = Game(player)

    selected_planet = initial_planet

    active_view = "main"
    build_main_nav()
    # build_map()
    # build_left_nav_menu()
    # build_bottom_nav_menu()


def build_main_nav():

    global left_nav, bottom_nav, main_nav, map_nav, navs_have_been_built

    left_nav = Frame(main_window, height=main_window.sh, width=200, background=conf.left_nav_background)
    bottom_nav = Frame(main_window, height=200, width=(main_window.sw-200), background=conf.bottom_nav_background)
    main_nav = Frame(main_window, height=main_window.sh-200, width=main_window.sw-200, background='black')
    map_nav = Frame(main_window, height=200, width=200, background=conf.left_nav_background)

    # build_bottom_nav_menu()
    # build_map()

    if navs_have_been_built:
        print "redrawing left nav"
        draw_left_nav_menu()
    else:
        build_planet_view()
        build_left_nav_menu()
        navs_have_been_built = True


def build_left_nav_menu():

    global left_nav, left_canvas

    left_nav.place(x=0, y=0)

    left = LeftNav(main_window, player, left_nav)


'''
    left_canvas = Canvas(left_nav)
    left_canvas.config(background=conf.left_nav_background, highlightthickness=0, height=main_window.sh, width=200)
    left_canvas.place(x=0, y=0)

    if conf.debug_lines == 1:
        left_canvas.create_line(0, 0, 200, main_window.sh, fill='red')
        left_canvas.create_line(200, 0, 0, main_window.sh, fill='red')

    # left nav values

    logo_image = Image.open(conf.title_image_path)
    logo_image.thumbnail([198, 48], Image.ANTIALIAS)
    logo_image_res = ImageTk.PhotoImage(logo_image)
    new_planet_image = logo_image_res
    planet_images.append(new_planet_image)
    label_logo = Label(left_canvas, image=logo_image_res)
    label_logo.config(background=conf.left_nav_background)
    label_logo.planet_image_res = logo_image_res           # keep a reference!
    label_logo.place(anchor='n', x=100, y=0)

    # build row set

    row = 0

    resources_start_y = 55
    resources_canvas = Canvas(left_canvas)
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
    left_buttons_canvas = Canvas(left_canvas)
    left_buttons_canvas.config(background=conf.left_nav_background,
                               height=200,
                               width=200,
                               highlightthickness=0,
                               border=0)
    left_buttons_canvas.place(anchor='n', x=100, y=left_buttons_start_y)

    button_next_planet = Button(left_buttons_canvas, text="Next Planet", padx=60
                                , highlightbackground=conf.left_nav_background
                                , command=button_next_planet_clicked)
    button_next_ship = Button(left_buttons_canvas, text="Next Ship"
                              , highlightbackground=conf.left_nav_background
                              , command=button_next_ship_clicked)
    button_home_planet = Button(left_buttons_canvas, text="Home Planet"
                                , highlightbackground=conf.left_nav_background
                                , command=button_home_planet_clicked)
    button_end_turn = Button(left_buttons_canvas, text="End Turn"
                             , highlightbackground=conf.left_nav_background
                             , command=button_end_turn_clicked)

    button_next_planet.grid(row=0, column=0, sticky='w,e')
    button_next_ship.grid(row=1, column=0, sticky='w,e')
    button_home_planet.grid(row=2, column=0, sticky='w,e')
    button_end_turn.grid(row=3, column=0, sticky='w,e')

    if conf.debug == 1:
        print "CreatedLine:", 0, " ", 0, " ", main_window.sw-200, " ", main_window.sh-200
        print "CreatedLine:", main_window.sw-200, " ", 0, " ", 0, " ", main_window.sh-200
        print "CurrWin0:", convert_coords_x(0), convert_coords_y(0)

    if conf.debug == 1:
        print "Displayed: left_nav,", main_window.sh, ",200"
'''


def button_next_planet_clicked():
    pass


def button_next_ship_clicked():
    pass


def button_home_planet_clicked():

    pass


def button_end_turn_clicked():
    pass


def build_bottom_nav_menu():

    global bottom_nav
    bottom_nav.place(x=200, y=(main_window.sh-200))

    if conf.debug == 1:
        print "Displayed: bottom_nav,200,", str(main_window.sw-200)


def build_map():

    global main_nav
    map_nav.place(x=main_window.sw-200, y=0)

    if conf.debug == 1:
        print "Displayed: map_nav,200,200"


def build_planet_view():

    if conf.debug == 1:
        print "Displayed: main_nav,", main_window.sh-200, ",", main_window.sh-200

    global main_nav, main_canvas, selected_planet

    main_nav.place(x=200, y=0)
    main_canvas = Canvas(main_nav)

    # draw corner lines
    if conf.debug_lines == 1:
        main_canvas.create_line(0, 0, main_window.sw-200, main_window.sh-200, fill='red')
        main_canvas.create_line(main_window.sw-200, 0, 0, main_window.sh-200, fill='red')

    if conf.debug == 1:
        print "CreatedLine:", 0, " ", 0, " ", main_window.sw-200, " ", main_window.sh-200
        print "CreatedLine:", main_window.sw-200, " ", 0, " ", 0, " ", main_window.sh-200
        print "CurrWin0:", convert_coords_x(0), convert_coords_y(0)

    # select the main planet
    if selected_planet == "":
        selected_planet = player.planets[0]

    main_canvas.config(width=main_window.sw-200, height=main_window.sh-200)
    main_canvas.config(background='black')
    main_canvas.config(highlightbackground=conf.main_background)
    main_canvas.config(highlightthickness=0)

    if conf.debug == 1:
        print "********************"
        print "********************"
        print "********************"

    # draw planets
    for planet in player.planets:
        if conf.debug == 1:
            print "init:", planet.loc.x, ",", planet.loc.y
        if planet == selected_planet:
            draw_planet_highlighted(planet)
        else:
            draw_planet(planet)

    finish_drawing_planets()


def planet_filter():
    global player
    to_remove = []
    for a in range(len(player.planets)):
        for b in range(len(player.planets)):
            if a != b:
                print "c:", a, ":", b
                if check_intersect(player.planets[a].loc, player.planets[b].loc):
                    to_remove = add_unique(to_remove, b)
                    # if conf.debug == 1:
                    #     print "Removing Planet, dist:", get_distance(player.planets[a].loc, player.planets[b].loc)

    to_remove.sort()
    for i in to_remove:
        print i

    for i in to_remove[::-1]:
        print "Removing: ", i
        player.planets.remove(player.planets[i])



    '''
    for planet_a in player.planets:
        for planet_b in player.planets:
            if check_intersect(planet_a.loc, planet_b.loc):
                player.planets.remove(planet_b)
                if conf.debug == 1:
                    print "Removed Planet"
    '''


def add_unique(array, item):

    in_array = False
    for i in array:
        if i == item:
            in_array = True

    if not in_array:
        array.append(item)

    return array


def check_intersect(loc1, loc2):
    size1 = loc1.size
    size2 = loc2.size

    distance = get_distance(loc1, loc2)

    if distance < loc1.size + loc2.size:
        return True
    else:
        return False


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
        return ice_planet_image_path
    elif terrain == 2:
        return rock_planet_image_path
    elif terrain == 3:
        return green_planet_image_path
    elif terrain == 4:
        return water_planet_image_path
    elif terrain == 5:
        return alien_planet_image_path
    else:
        return alien_planet_image_path


def convert_coords_x(x):
    return ((main_window.sw - 200) / 2) + x


def convert_coords_y(y):
    return ((main_window.sh - 200) / 2) + y


def convert_coords_name(y, size):
    return ((main_window.sh - 200) / 2) + y - (size / 2) - conf.planet_name_height


def finish_drawing_planets():
    main_canvas.pack(fill='both')
    if conf.debug == 1:
        print "PlanetGen: NewLoc:", player.new_loc
        print "PlanetGen: Failed:", player.failed_to_find
        print "WindowSize:", main_window.sw, ":", main_window.sh
        print "Total planets:", len(player.planets)


def draw_planet(planet):
    global main_nav, main_canvas, label, planet_images

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
    label = Label(main_canvas, image=planet_image_res)
    label.config(background='black')
    label.grid()
    label.planet_image_res = planet_image_res           # keep a reference!
    label.place(anchor=CENTER, x=new_x, y=new_y)

    label_name = Label(main_canvas, text=planet.name, fg='white', bg='black', borderwidth=1, highlightthickness=0)
    label_name.place(anchor=CENTER, x=new_x, y=name_y)

    if conf.debug == 1:
        print "Drawing planet: [", planet.name, ",", new_x, ",", new_y, ",", planet.loc.size, ",", color, "]"


def draw_planet_highlighted(planet):
    global main_nav, main_canvas, label, planet_images

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
    label_planet = Label(main_canvas, image=planet_image_res)
    label_planet.config(background='black')
    label_planet.planet_image_res = planet_image_res           # keep a reference!
    label_planet.place(anchor=CENTER, x=new_x, y=new_y)

    label_name = Label(main_canvas, text=planet.name, fg='red', bg='black', borderwidth=1, highlightthickness=0)
    label_name.place(anchor=CENTER, x=new_x, y=name_y)

    if conf.debug == 1:
        print "Drawing planet: [", planet.name, ",", new_x, ",", new_y, ",", planet.loc.size, ",", color, "]"


if __name__ == '__main__':
    # globalize the main window
    root = Tk()
    main_window = MainWindow(root)
    main()

