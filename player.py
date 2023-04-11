import pygame

self = pygame.sprite.Sprite

def start():
    self.sprite_sheet = pygame.image.load("imports/BlueWizard/2BlueWizardIdle/spritesheet.png")
    self.image = get_image(self, 0, 0)
    self.rect = self.image.get_rect()

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
