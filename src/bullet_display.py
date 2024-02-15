import pygame

# Define colors
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0,200,0)
BLUE = (0,0,200)

class BulletDisplay:
    def __init__(self):
        self.counts = {RED: 0, GREEN: 0, BLUE: 0}
        self.font = pygame.font.Font(None, 24)

    def draw(self, surface):
        for i, (color, count) in enumerate(self.counts.items()):
            text = self.font.render(f"{count}", True, BLACK)
            surface.blit(text, (720, 100 + i * 30))
            pygame.draw.circle(surface, color, (750, 110 + i * 30), 10)

    def increment(self, color):
        self.counts[color] += 1

    def decrement(self, color):
        if self.counts[color] > 0:
            self.counts[color] -= 1

    def reset(self):
        self.counts = {RED: 0, GREEN: 0, BLUE: 0}