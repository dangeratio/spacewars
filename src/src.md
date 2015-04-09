# src.md

This file provides a structure view of the codebase (at least the intended structure of the codebase)

Legend

    (M) - Model
    (V) - View
    (C) - Controller

Structure

    ApplicationController (C)
        MainController (C)
            main_screen (V)
            PopupController (C)
                popup (V)
            LeftNavController (C)
                left_nav (V)
            MainNavController (C)
                main_nav (V)
            MapNavController (C)
                map_nav (V)
            IntroController (C)
                intro_screen (V)
        config (M)
        game (M)
            player (M)
                planet(s) (M)
                ship(s) (M)

