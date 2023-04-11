import pygame

image_test = pygame.sprite.Sprite

def start():
    def get_image(_image_test, x, y):
        image = pygame.Surface([32, 32])
        image.blit(_image_test.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image

    image_test.sprite_sheet = pygame.image.load("imports/BlueWizard/2BlueWizardIdle/spritesheet.png")
    image_test.image = get_image(image_test, 0, 0)
    image_test.rect = image_test.image.get_rect()