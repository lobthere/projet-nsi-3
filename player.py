import pygame

velocity_for_move = 1

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y, image_path):
        super().__init__()
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
        self.image = pygame.image.load(image_path)
    
    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

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