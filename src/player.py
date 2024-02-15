import pygame

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./assets/tank.png')
        self.rect = self.image.get_rect()
        self.rect.center = (50, 144)
        self.bullet_colors = []
        self.speed = 6
        
        # default
        self.up = False
        self.down = False
        self.left = False
        self.right = True   

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

        # Make sure the player stay inside the screen border
        screen_rect = pygame.display.get_surface().get_rect()
        if not screen_rect.contains(self.rect):
            self.rect = previous_rect

    def collect(self, bullet_color):
        self.bullet_colors.append(bullet_color)


    def reset_position(self):
        self.rect.center = (50, 144)
        self.bullet_colors = []
        self.reset_rotation()

    def reset_rotation(self):
        self.image = pygame.image.load('./assets/tank.png') 
        self.up = False
        self.down = False
        self.left = False
        self.right = True 