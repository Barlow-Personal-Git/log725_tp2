import pygame

from src.item.bullet import Bullet

RED = (200, 0, 0)
GREEN = (0,200,0)
BLUE = (0,0,200)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/tank.png')
        self.rect = self.image.get_rect()
        self.rect.center = (50, 144)
        self.ammo = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        self.speed = 6
        
        # default
        self.up = False
        self.down = False
        self.left = False
        self.right = True   
        self.direction = 'right'

    def update(self):
        keys = pygame.key.get_pressed()

        # Copy the previous rect
        previous_rect = self.rect.copy()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            if self.up and not self.left:
                self.image = pygame.transform.rotate(self.image, 90)
                self.left = True
                self.up = False
            elif self.down and not self.left:
                self.image = pygame.transform.rotate(self.image, -90)
                self.left = True
                self.down = False
            elif self.right and not self.left:
                self.image = pygame.transform.rotate(self.image, 180)
                self.left = True
                self.right = False

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            if self.up and not self.right:
                self.image = pygame.transform.rotate(self.image, -90)
                self.right = True
                self.up = False
            elif self.down and not self.right:
                self.image = pygame.transform.rotate(self.image, 90)
                self.right = True
                self.down = False
            elif self.left and not self.right:
                self.image = pygame.transform.rotate(self.image, 180)
                self.right = True
                self.left = False

        if keys[pygame.K_UP] :
            self.rect.y -= self.speed
            if self.right and not self.up :
                self.image = pygame.transform.rotate(self.image, 90)
                self.up = True
                self.right = False
            elif self.left and not self.up:
                self.image = pygame.transform.rotate(self.image, -90)
                self.up = True
                self.left = False
            elif self.down and not self.up:
                self.image = pygame.transform.rotate(self.image, 180)
                self.up = True
                self.down = False
                
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.up and not self.down:
                self.image = pygame.transform.rotate(self.image, 180)
                self.down = True
                self.up = False
            elif self.left and not self.down:
                self.image = pygame.transform.rotate(self.image, 90)
                self.down = True
                self.left = False
            elif self.right and not self.down:
                self.image = pygame.transform.rotate(self.image, -90)
                self.down = True
                self.right = False
        self.update_direction()

        # Make sure the player stay inside the screen border
        screen_rect = pygame.display.get_surface().get_rect()
        if not screen_rect.contains(self.rect):
            self.rect = previous_rect

    def collect(self, bullet_color):
        if bullet_color == RED:
            self.ammo["red"] += 1
        elif bullet_color == GREEN:
            self.ammo["green"] += 1
        elif bullet_color == BLUE:
            self.ammo["blue"] += 1

    def reset_position(self):
        self.rect.center = (50, 144)
        self.ammo = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        self.reset_rotation()

    def reset_rotation(self):
        self.image = pygame.image.load('./assets/tank.png') 
        self.up = False
        self.down = False
        self.left = False
        self.right = True 

    def shoot(self, bullet_color):
        bullet_sound = pygame.mixer.Sound('assets/music/cg1.wav')
        if bullet_color == RED and self.ammo["red"] > 0:
            self.ammo["red"] -= 1
            bullet_sound.play()
            return Bullet(RED, self.rect.center, self.direction)
        elif bullet_color == GREEN and self.ammo["green"] > 0:
            self.ammo["green"] -= 1
            bullet_sound.play()
            return Bullet(GREEN, self.rect.center, self.direction)
        elif bullet_color == BLUE and self.ammo["blue"] > 0:
            self.ammo["blue"] -= 1
            bullet_sound.play()
            return Bullet(BLUE, self.rect.center, self.direction)
        return None
    
    def update_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction = 'down'
        elif keys[pygame.K_LEFT]:
            self.direction = 'left'
        elif keys[pygame.K_RIGHT]:
            self.direction = 'right'