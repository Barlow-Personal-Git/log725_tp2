import pygame

class Green_Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load('./assets/green.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = (0, 200, 0)
            
    def reset_position(self, x, y):
        self.rect.topleft = (x, y)