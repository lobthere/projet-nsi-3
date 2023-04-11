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
    COLOR_BACKGROUND_SCREEN = (255, 255, 255)

    """
    ------creation de la fenetre------
    """
    init = game.initialisation(DISPLAY_X, DISPLAY_Y, COLOR_BACKGROUND_SCREEN)           #cree la fenetre a partir d une methode dans le fichier game.py
    surface = init[0]                                                                   #on recupere la surface dans une variable afin de la reutiliser plus tard
    group = init[1]                                                                     #meme chose pour group
    game.run(surface, group)                                                            #lance la boucle principal du jeu