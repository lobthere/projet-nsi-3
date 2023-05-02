import pygame, pyscroll, pytmx
from pytmx.util_pygame import load_pygame

class Game:
    def __init__(self, display_x, display_y, ) :
        #la fenetre
        self.surface = pygame.display.set_mode((display_x, display_y))
        pygame.display.set_caption("jeu de conversion")   

        #charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('map/map1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.surface.get_size())
        map_layer.zoom = 0.1
        
        #dessiner le grp de calques
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    def run(self):
        running = True                              

        while running:

            self.group.draw(self.surface)
            pygame.display.flip()

            for event in pygame.event.get():        
                if event.type == pygame.QUIT:       
                    running = False
        pygame.quit()