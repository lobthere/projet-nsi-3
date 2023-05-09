import pygame, pyscroll, pytmx
from pytmx.util_pygame import load_pygame
from player import *

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
        OwO_to_load_image = []
        for i in range(20):
            b = str(i)
            if len(b) == 1:
                OwO_to_load_image.append(f"imports\BlueWizard\OwO\Chara_BlueIdle0000{i}.png")
            else:
                OwO_to_load_image.append(f"imports\BlueWizard\OwO\Chara_BlueIdle000{i}.png")

        player = Player(320, 240, 0, 0, OwO_to_load_image)
        running = True                              

        while running:

            self.group.draw(self.surface)
            player.update(self.surface)
            player.draw(self.surface)
            pygame.display.flip()

            for event in pygame.event.get():        
                if event.type == pygame.QUIT:       
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.move_left()
                    elif event.key == pygame.K_RIGHT:
                        player.move_right()
                    elif event.key == pygame.K_UP:
                        player.move_up()
                    elif event.key == pygame.K_DOWN:
                        player.move_down()
                else:
                    player.stop_movement()
        pygame.quit()