# game.py
# description: Main model object, all gameplay models are below
#
# Game*
#     Player
#         Ship
#         Planet

from Models.player import *


class Game(object):
    def __init__(self):

        self.player = Player()
        pass