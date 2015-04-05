import random
from configfile import *
from math import cos, sin


conf = ConfigFile()
data = DataFile()


class Planet(object):
    def __init__(self, name, population, metals, food, terrain, loc, owned):

        self.population = population
        self.metals = metals
        self.food = food
        self.terrain = terrain
        self.loc = loc
        self.name = name
        self.owned = owned

        if conf.debug == 1:
            print "Created Planet: [ x:", self.loc.x, ", y:", self.loc.y, ", pop:", self.population, \
                ", metals:", self.metals, ", food:", self.food, ", terrain:", str(self.terrain), "]"


class GeneratePlanet(Planet):
    def __init__(self, name, loc):
        super(GeneratePlanet, self).__init__(name, 0, generate_metals(),
                                             generate_food(), generate_terrain(), loc, 'none')


class Location(object):
    def __init__(self, x, y, size, distance):
        self.x = x
        self.y = y
        self.distance = distance
        self.size = size


class GenerateLocation(Location):
    def __init__(self):

        distance = random.randint(0, conf.max_distance)
        x = distance * cos(distance)
        y = distance * sin(distance)

        super(GenerateLocation, self).__init__(x, y, generate_planet_size(), distance)


class InitialPlanet(Planet):
    def __init__(self):
        loc = Location(0, 0, initial_planet_size(), 0)
        super(InitialPlanet, self).__init__(generate_planet_name(), initial_population()
                                            , initial_metals(), initial_food(), initial_terrain(), loc, 'player')


def initial_population():
    return 100


def initial_metals():
    return random.randint(50, 100)


def initial_food():
    return random.randint(50, 100)


def generate_metals():
    return random.randint(0, 100)


def generate_food():
    return random.randint(0, 100)


def generate_planet_size():
    return random.randint(10, 100)


def initial_planet_size():
    return random.randint(50, 60)


def initial_terrain():
    return random.randint(1, 3)


def generate_terrain():
    # Planet Terrains
    # 1 Ice
    # 2 Rock
    # 3 Green
    # 4 Water
    # 5 Alien
    return random.randint(1, 5)


def convert_angles_to_loc(angle, distance, size):

    x = distance * cos(angle)
    y = distance * sin(angle)

    loc = Location(x, y, size)
    return loc


def generate_planet_name():
    return data.planet_names[random.randint(0, len(data.planet_names)-1)]