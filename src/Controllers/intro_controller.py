# intro_controller.py
# description: this is the controller for the intro screen
#
# ApplicationController
#     MainController
#         IntroController*
#         LeftNavController
#         MainNavController
#         MapNavController

from Views.intro_view import IntroView



class IntroController(object):
    def __init__(self, parent):

        self.parent = parent
        self.app = self.parent.app
        self.view = IntroView(self, self.parent.view)
        self.enabled = True

    def message(self, message):

        if self.enabled:

            self.app.debug_messaging("IntroController|Message|" + message)

            if message == 'display intro':
                self.view.build()
                self.view.draw()
            if message == 'refresh':
                self.view.draw()

    def event_button_new_game(self):

        self.view.hide()
        self.parent.message('new game')
        self.enabled = False

    def event_button_load_game(self):
        pass

    def event_button_quit(self):
        # do any needed cleanup
        exit()
