import os, sys, inspect
from Tkinter import Tk

from Controllers.app import *


def main():
    #init_intro_nav()
    #draw_intro_nav()
    #root.mainloop()

    application.view_intro.init_intro_nav()
    application.view_intro.draw_intro_nav()
    root.mainloop()



if __name__ == '__main__':

    #root = Tk()
    #main_window = MainWindow(root)
    #main()

    root = Tk()
    application = Application(root)
    main()

