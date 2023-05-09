import pygame

velocity_for_move = 1

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y, image_path):
        super().__init__()
        self.OwO = image_path
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
        self.image = pygame.image.load(image_path[0])
        self.i = 0
    
    def update(self, surface):
        img_2 = pygame.image.load(self.OwO[self.i])
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        surface.blit(self.image, self.position)
        self.i += 1
        if self.i == 20:
            self.i = 0

    def draw(self, surface):
        surface.blit(self.image, self.position)

    def move_left(self):
        self.velocity = (-1 * (velocity_for_move), self.velocity[1])

    def move_right(self):
        self.velocity = (velocity_for_move, self.velocity[1])

    def move_up(self):
        self.velocity = (self.velocity[0], -1 * (velocity_for_move))
    
    def move_down(self):
        self.velocity = (self.velocity[0], velocity_for_move)

    def stop_movement(self):
        self.velocity = (0, 0)