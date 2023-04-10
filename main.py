import pygame


pygame.init()   #initialise pygame

"""
--------la fenetre--------
"""
DISPLAY_X = 1600                            #dimension de la fenetre en x
DISPLAY_Y = 900                             #dimension de la fenetre en y
COLOR_BACKGROUND_SCREEN = (255, 255, 255)   #choisit la couleur de la fenetre

surface = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))   #genere la fenetre
pygame.display.set_caption("jeu de conversion")             #met le nom de la fenetre

surface.fill(COLOR_BACKGROUND_SCREEN)       #applique la couleur predefinie a la fenetre
pygame.display.flip()                       #met a jour sur la fenetre

"""
--------La boucle du jeu--------
"""
running = True                              #definie l'etat du programme

while running:
    for event in pygame.event.get():        #recupere tout les evenements present sur la fenetre
        if event.type == pygame.QUIT:       #permet de fermer le programme si on clic sur la croix
            running = False                 #on change l'etat du programme

pygame.quit()                               #met a jour la fenetre