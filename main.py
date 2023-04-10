import pygame
import game

if __name__ == '__main__':
    pygame.init()               #initialise pygame

    """
    ------les parametres de la fenetre------
    """
    DISPLAY_X = 1600
    DISPLAY_Y = 900
    COLOR_BACKGROUND_SCREEN = (255, 255, 255)

    """
    ------creation de la fenetre------
    """
    surface = game.initialisation(DISPLAY_X, DISPLAY_Y, COLOR_BACKGROUND_SCREEN)        #cree la fenetre a partir d une methode dans le fichier game.py
    game.carte(surface.get_size())
    temp = game.group(game.carte)
    game.run(surface, temp)