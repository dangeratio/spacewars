import random
from configfile import *


conf = ConfigFile()
data = DataFile()


class Ship(object):
    def __init__(self, location, speed, attack, defense, storage, seats):
        self.location = location
        self.speed = speed
        self.attack = attack
        self.defense = defense
        self.storage = storage
        self.seats = seats

        if conf.debug == 1:
            print "Created Ship: [ speed:", speed, ", attack:", attack, ", defense:", defense, \
                ", storage:", storage, ", seats:", seats, "]"


class ShipLocation(object):
    def __init__(self, from_planet, to_planet):
        self.from_planet = from_planet
        self.to_planet = to_planet
        if from_planet == to_planet:
            self.on_planet = True
            self.planet = from_planet


class InitialShip(Ship):
    def __init__(self, initial_planet):
        location = ShipLocation(initial_planet, initial_planet)
        super(InitialShip, self).__init__(location, initial_speed(), initial_attack()
                                          , initial_defense(), initial_storage(), initial_seats())


def initial_speed():
    return random.randint(5,10)


def initial_attack():
    return 1


def initial_defense():
    return 1


def initial_storage():
    return 0


def initial_seats():
    return 0


