from Controllers.application_controller import *

'''
def main():
    #init_intro_nav()
    #draw_intro_nav()
    #root.mainloop()

    application.view_intro.init_intro_nav()
    application.view_intro.draw_intro_nav()
    root.mainloop()

'''

if __name__ == '__main__':

    # initiate application object
    application = ApplicationController()

    # enter the run loop
    application.main_controller.view.root.mainloop()

