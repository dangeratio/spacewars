# _game.py
# description: this contains an old set of game code, no longer used, only for reference at this point
#
#


from Tkinter import Tk, Frame, Label, Button, Canvas, CENTER
from PIL import Image, ImageTk, ImageDraw
from math import sqrt

from ship import *
from planet import *
from player import *
from configfile import *
from left_nav import *

# load config file
'''
conf = ConfigFile()
conf.print_debug()
'''
'''
# colors and intro
intro_padding_height = 77.5
navs_have_been_built = False
'''

'''
# initial generation variables
selected_planet = ""
selected_ship = ""

# planet images
planet_images = []

# init action scheduler
pending_actions = []

'''

'''
active_view variable controls what view is displayed.  These are the values:
- intro: this is the first screen a user sees when they enter the game
- main: this is the main game screen the user will spend most of the time in the game playing
''' '''
active_view = "intro"
'''

'''
main_canvas_has_been_created = False
'''

'''

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

        self.parent.geometry('%dx%d+%d+%d' % (self.sw, self.sh, 0, 0))

    def remove_this(self):
        self.frame.destroy()

    def refresh(self):
        if active_view == "intro":
            draw_intro_nav()
        elif active_view == "main":
            build_main_nav()
'''

'''
class ContainerFrame(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, background=conf.window_background)
        self.parent = parent
        self.update()

    def remove_this(self):
        self.frame.destroy()

'''

#
# general window handling
#

'''
def click(event):
    print "clicked at", event.x, event.y

'''

'''
def resize(event):

    global main_window
    global active_view

    main_window.sw = event.width
    main_window.sh = event.height

    if main_window.sw <= 500:
        main_window.sw = 500

    if main_window.sh <= 500:
        main_window.sh = 500

    if conf.debug == 1:
        print "(", main_window.sw, ",", main_window.sh, ",", active_view, ")"

    main_window.refresh()

'''
'''
def main():
    init_intro_nav()
    draw_intro_nav()

    # if len(pending_actions) > 0:
    #     for action in pending_actions:
    #         if action == 'invoke_new_game':
    #             button_new_game.invoke()

    root.mainloop()

'''
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

'''
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
'''
'''
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


'''
'''

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


    ######################################################
    #
    # remove next line for normal operation
    #
    ######################################################

'''
'''

def quitting():
    # do any needed cleanup
    exit()


def event_button_new_game():

    global active_view

    hide_intro_nav()
    active_view = "main"

    global player, selected_planet, game

    # initial_planet = InitialPlanet()
    # initial_ship = InitialShip(initial_planet)
    # player = InitialPlayer(initial_planet, initial_ship)

    player = InitialPlayer()
    player.generate_initial_planet()
    player.generate_initial_ship(player.home_planet_name)

    for i in range(conf.planets_to_generate):
        player.generate_new_planet()
    game = Game(player)

    selected_planet = player.planets[0]

    active_view = "main"
    build_main_nav()
    # build_map()
    # build_left_nav_menu()
    # build_bottom_nav_menu()



def event_button_load_game():
    pass


def event_button_quit():
    quitting()
'''

# main game handling

'''
class Game(object):
    def __init__(self, player):
        self.player = player
'''
'''
def build_main_nav():

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
'''
'''
def build_left_nav_menu():

    global left_nav, left_canvas, left

    left_nav.place(x=0, y=0)

    left = LeftNav(main_window, player, left_nav)
'''
'''
# no longer using a bottom nav

def build_bottom_nav_menu():

    global bottom_nav
    bottom_nav.place(x=200, y=main_window.sh)

    if conf.debug == 1:
        print "Displayed: bottom_nav,200,", str(main_window.sw)
'''
'''
def build_map():

    global main_nav
    map_nav.place(x=main_window.sw-200, y=0)
    if conf.debug == 1:
        print "Displayed: map_nav,200,200"
'''
'''
def build_planet_view():

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
'''
'''
def redraw_planet_view():

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
'''


'''
def check_intersect(loc1, loc2):
    size1 = loc1.size
    size2 = loc2.size

    distance = get_distance(loc1, loc2)

    if distance < loc1.size + loc2.size:
        return True
    else:
        return False
'''
'''
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


def finish_drawing_planets():

    global main_canvas, main_window

    main_canvas.pack(fill='both')
    if conf.debug == 1:
        # print "Drawing: NewLoc:", player.new_loc
        # print "Drawing: Failed:", player.failed_to_find
        print "WindowSize:", main_window.sw, ":", main_window.sh
        # print "PlanetsDrawn:", len(player.planets)
'''
'''
def select_planet(event, planet):

    global main_window

    # w = event.widget
    player.selected_planet = planet
    if conf.debug == 1:
        print "SelectingPlanet:", planet.name
    main_window.refresh()
'''
'''
def draw_planet(planet):

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


def draw_planet_highlighted(planet):

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
'''
'''
if __name__ == '__main__':
    # globalize the main window
    root = Tk()
    main_window = MainWindow(root)
    main()

'''