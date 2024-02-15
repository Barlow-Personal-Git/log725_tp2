import pygame

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load('./assets/floor.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
