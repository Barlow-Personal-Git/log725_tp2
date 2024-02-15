import pygame

class Blue_Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load('./assets/blue.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = (0, 0, 200)

    def reset_position(self, x, y):
        self.rect.topleft = (x, y)
