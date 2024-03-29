import pygame

class Ammo:
    color = (0,0,0)
    radius = 10
    speed = 8

    def __init__(self,color, pos):
        self.color = color
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=pos)
    
    def reset_position(self, x, y):
        self.rect.topleft = (x, y)

