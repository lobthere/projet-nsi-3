import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"                                       #cache le message de bienvenue de pygame

import pygame
import game


if __name__ == '__main__':
    pygame.init()                                                                       #initialise pygame
    """
    ------les parametres de la fenetre------
    """
    
    DISPLAY_X = 1600
    DISPLAY_Y = 900

    """
    ------creation de la fenetre------
    """
    game = game.Game(DISPLAY_X, DISPLAY_Y)
    game.run()