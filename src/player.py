from math import sqrt
from configfile import ConfigFile
from planet import *


conf = ConfigFile()
data = DataFile()


class Player(object):
    def __init__(self, name, player_credits, planet_list, ship_list, enemies_list, allies_list):
        self.name = name
        self.credits = player_credits
        self.planets = planet_list
        self.ships = ship_list
        self.enemies = enemies_list
        self.allies = allies_list
        self.new_loc = 0
        self.failed_to_find = 0
        self.owned_planets = []

        if conf.debug == 1:
            print "Created Player: [ name:", name, "]"

    def generate_new_planet(self):

        valid_name = False
        while not valid_name:
            name = generate_planet_name()
            valid_name = self.check_name(valid_name)

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

    def check_name(self, name):
        return_val = True
        for planet in self.planets:
            if name == planet.name:
                return_val = False
                if conf.debug == 1:
                    print "PlanetGen: Need New Name"
        return return_val


class InitialPlayer(Player):
    def __init__(self, initial_planet, initial_ship):
        super(InitialPlayer, self).__init__("User", 1000000, [initial_planet], [initial_ship], [], [])
        self.owned_planets = [0]      # initial planet's id


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
