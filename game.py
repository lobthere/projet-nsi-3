import pygame, pytmx, pyscroll

def initialisation(display_x, display_y, color_background_screen) :
    """
    fenetre(): cree la fenetre du jeu avec ces caracteristiques
    DISPLAY_X: dimension de la fenetre en x
    DISPLAY_Y: dimension de la fenetre en y
    COLOR_BACKGROUND_SCREEN: couleur du fond de la fenetre (3 valeurs en code rgb)
    """

    surface = pygame.display.set_mode((display_x, display_y))   #genere la fenetre
    pygame.display.set_caption("jeu de conversion")             #met le nom de la fenetre

    surface.fill(color_background_screen)       #applique la couleur predefinie a la fenetre
    pygame.display.flip()                       #met a jour sur la fenetre
    
    return surface

def run(surface, map):
    running = True                              #definie l'etat du programme

    while running:
        map.draw(surface)
        pygame.display.flip()
        for event in pygame.event.get():        #recupere tout les evenements present sur la fenetre
            if event.type == pygame.QUIT:       #permet de fermer le programme si on clic sur la croix
                running = False                 #on change l'etat du programme

    pygame.quit()                               #met a jour la fenetre

def carte(taille_map):
    tmx_data = pytmx.util_pygame.load_pygame('map\map1.tmx')
    map_data = pyscroll.data.TiledMapData(tmx_data)
    map_layer = pyscroll.orthographic.BufferedRenderer(map_data, taille_map)

    return map_layer

def group(map_layer):
    return pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
