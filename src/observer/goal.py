import pygame
from src.observer.observer import Observer

BLACK = (0, 0, 0)
RED = (200, 0, 0)

class Goal(pygame.sprite.Sprite):

    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def on_player_reach_goal(self):
        print("Congratulations! You reached the goal!")


    def display_popup(self, screen, message):
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, BLACK)
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        pygame.draw.rect(screen, RED, (text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20))
        pygame.draw.rect(screen, BLACK, (text_rect.x - 10, text_rect.y - 10, text_rect.width + 20, text_rect.height + 20), 2)
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.delay(1000)