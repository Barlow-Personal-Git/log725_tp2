import pygame

class Bullet:
    color = (0,0,0)
    radius = 10

    def __init__(self,color, player_position, direction):
        self.color = color
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.speed = 8 
        self.rect = self.image.get_rect()
        self.reset_position(*player_position)
        self.direction = direction
        self.set_velocity()
        self.should_remove = False
    
    def reset_position(self, x, y):
        self.rect.topleft = (x, y)

    def update(self, walls, blocks):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        wall_collision = pygame.sprite.spritecollideany(self, walls)
        if wall_collision:
            self.should_remove = True

        # Check collision with blocks
        block_collision = pygame.sprite.spritecollideany(self, blocks)
        if block_collision:
            if block_collision.color == self.color: 
                block_collision.kill() 
            self.should_remove = True

        # Check if bullet is out of screen
        screen_rect = pygame.display.get_surface().get_rect()
        if not screen_rect.contains(self.rect):
            self.should_remove = True

    def set_velocity(self):
        if self.direction == 'up':
            self.speed_x = 0
            self.speed_y = -self.speed
        elif self.direction == 'down':
            self.speed_x = 0
            self.speed_y = self.speed
        elif self.direction == 'left':
            self.speed_x = -self.speed
            self.speed_y = 0
        elif self.direction == 'right':
            self.speed_x = self.speed
            self.speed_y = 0