import pygame

pygame.init()

DISPLAY_X = 1600
DISPLAY_Y = 900

color_background_screen = (255, 255, 255)
surface = pygame.display.set_mode((DISPLAY_X, DISPLAY_Y))
pygame.display.set_caption("jeu de conversion")
surface.fill(color_background_screen)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.display.update()