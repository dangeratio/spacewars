# player.py
# description: middle model object under player
#
# Game
#     Player
#         Ship
#         Planet


from math import sqrt
from Models.planet import *
from Models.ship import *


data = DataFile()


class Player(object):
    def __init__(self, parent, name, player_credits, planet_list, ship_list, enemies_list, allies_list):

        self.parent = parent
        self.app = parent.app
        self.name = name
        self.credits = player_credits
        self.planets = []
        self.ships = []
        self.enemies = enemies_list
        self.allies = allies_list
        self.new_loc = 0
        self.failed_to_find = 0
        self.owned_planets = []
        self.home_planet_name = 0
        self.selected_planet = 0
        self.selected_ship = 0

        if conf.debug == 1:
            print "Created Player: [ name:", name, "]"

    def generate_ship_at_planet(self, planet):

        checking_name = True
        while checking_name:
            valid_name = True
            name = generate_ship_name()
            for ship in self.ships:
                if ship.name == name:
                    valid_name = False
            if valid_name:
                checking_name = False

        new_ship = GenerateShip(name, planet)
        self.ships.append(new_ship)

    def generate_initial_ship(self):

        # valid_name = False
        # while not valid_name:
        #     name = generate_ship_name()
        #     valid_name = self.check_ship_name(valid_name)

        name = generate_ship_name()
        new_ship = InitialShip(name, self.selected_planet.name)
        self.ships.append(new_ship)

    def generate_initial_planet(self):

        new_planet = InitialPlanet()
        self.planets.append(new_planet)
        new_planet_id = len(self.planets)-1
        self.owned_planets.append(new_planet_id)      # initial planet's id
        self.home_planet_name = self.planets[0].name
        self.selected_planet = self.planets[0]

    def generate_new_planet(self):

        checking_name = True
        while checking_name:
            valid_name = True
            name = generate_planet_name()
            for planet in self.planets:
                if planet.name == name:
                    valid_name = False
            if valid_name:
                checking_name = False

        valid_loc = False
        attempts = 0
        while not valid_loc:
            loc = GenerateLocation()
            valid_loc = self.check_location(loc)
            attempts += 1
            if attempts > 10:
                print "PlanetGen: Failed to find loc"
                self.failed_to_find += 1
                break

        if attempts <= 10:
            new_planet = GeneratePlanet(name, loc)
            self.planets.append(new_planet)

    def check_location(self, loc):
        return_val = True
        for planet in self.planets:
            touch_distance = sqrt((loc.size**2)*2) + sqrt((planet.loc.size**2)*2)

            if touch_distance >= get_distance(loc, planet.loc):
                return_val = False
                if conf.debug == 1:
                    print "PlanetGen: Need New Loc"
                self.new_loc += 1
        return return_val

    def check_planet_name(self, name):
        return_val = True
        for planet in self.planets:
            if name == planet.name:
                return_val = False
                if conf.debug == 1:
                    print "PlanetGen: Need New Name"
        return return_val

    def check_ship_name(self, name):
        return_val = True
        for ship in self.ships:
            if name == ship.name:
                return_val = False
                if conf.debug == 1:
                    print "ShipGen: Need New Name"
        return return_val

    def get_ship(self, ship_name):
        for ship in self.ships:
            if ship.name == ship_name:
                return ship
        return -1


class InitialPlayer(Player):
    def __init__(self, parent):
        super(InitialPlayer, self).__init__(parent, "User", 1000000, [], [], [], [])

        # create players initial ship and planet
        self.generate_initial_planet()
        self.generate_initial_ship()

        # create initial planets in game
        for i in range(self.app.conf.planets_to_generate):
            self.generate_new_planet()

def check_intersect(loc1, loc2):
    size1 = loc1.size
    size2 = loc2.size

    distance = get_distance(loc1, loc2)

    if distance < loc1.size + loc2.size:
        return True
    else:
        return False


def get_distance(loc1, loc2):
    x1, y1, size1 = loc1.x, loc1.y, loc1.size
    x2, y2, size2 = loc2.x, loc2.y, loc2.size

    return sqrt((x1-x2)**2 + (y1-y2)**2)


def generate_planet_name():
    return data.planet_names[random.randint(0, len(data.planet_names)-1)]


def generate_ship_name():
    return data.ship_names[random.randint(0, len(data.ship_names)-1)]
