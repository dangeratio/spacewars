# intro_controller.py
# description: this is the controller for the intro screen
#
# ApplicationController
#     IntroController*
#     MainController
#         LeftNavController
#         MainNavController
#         MapNavController

class IntroController(object):
    def __init__(self, application_controller):
        pass

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
