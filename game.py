import pygame, pyscroll, pytmx
from pytmx.util_pygame import load_pygame
from player import start

def initialisation(display_x, display_y, color_background_screen) :
    """
    fenetre(): cree la fenetre du jeu avec ces caracteristiques
    DISPLAY_X: dimension de la fenetre en x
    DISPLAY_Y: dimension de la fenetre en y
    COLOR_BACKGROUND_SCREEN: couleur du fond de la fenetre (3 valeurs en code rgb)
    """


    surface = pygame.display.set_mode((display_x, display_y))   #genere la fenetre
    pygame.display.set_caption("jeu de conversion")             #met le nom de la fenetre

    surface.fill(color_background_screen)                       #applique la couleur predefinie a la fenetre
    
    pygame.display.flip()                                       #met a jour sur la fenetre

    taille_map = surface.get_size()                             #assigne la taille de la map
    tmx_data = load_pygame('map\map1.tmx')                      #charge la premiere carte
    map_data = pyscroll.data.TiledMapData(tmx_data)             
    map_layer = pyscroll.orthographic.BufferedRenderer(map_data, taille_map)            #
    map_layer.zoom = 0.1                                                                #applique un dezoom sur le monde

    player = start()

    group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)                #cree la carte et lui assigne un plan
    group.add(player)

    return [surface, group]         #retourne plusieurs variables sous la forme d une liste


def run(surface, map_layer):
    running = True                              #definie l'etat du programme

    while running:
        map_layer.draw(surface)                 #applique la carte sur l'ecran (surface)
        pygame.display.flip()                   #met a jout

        for event in pygame.event.get():        #recupere tout les evenements present sur la fenetre
            if event.type == pygame.QUIT:       #permet de fermer le programme si on clic sur la croix
                running = False                 #on change l'etat du programme

    pygame.quit()                               #met a jour la fenetre