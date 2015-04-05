from ConfigParser import SafeConfigParser


class ConfigFile(object):
    def __init__(self):

        # load config file

        parser = SafeConfigParser()
        parser.read('config.ini')

        # save config

        self.debug = int(parser.get('game', 'debug'))
        self.debug_lines = int(parser.get('game', 'debug_lines'))
        self.version = parser.get('game', 'version')
        self.planets_to_generate = int(parser.get('game', 'initial_planets_to_generate'))
        self.max_distance = int(parser.get('game', 'initial_planet_max_distance'))
        self.planet_name_height = int(parser.get('game', 'planet_name_height'))

        self.window_background = parser.get('backgrounds', 'window_background')
        self.main_background = parser.get('backgrounds', 'main_background')
        self.black_color = parser.get('backgrounds', 'black_color')
        self.left_nav_background = parser.get('backgrounds', 'left_nav_background')
        self.intro_background = parser.get('backgrounds', 'intro_background')
        self.bottom_nav_background = parser.get('backgrounds', 'bottom_nav_background')
        self.title_image_path = parser.get('backgrounds', 'title_image_path')



    def print_debug(self):
        if self.debug:
            print "Config File Loaded [debug:", self.debug, ", version:", self.version, "]"


class DataFile(object):
    def __init__(self):

        # load data file

        parser = SafeConfigParser()
        parser.read('data.ini')

        # save data

        self.planet_names = parser.get('planet', 'names').split(", ")
        self.ship_names = parser.get('ship', 'names').split(", ")

        print "Planet Names Loaded:", len(self.planet_names)
        print "Ship Names Loaded:", len(self.ship_names)

