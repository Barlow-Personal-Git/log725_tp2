import pygame
import sys
from src.player import Player
from src.block.wall import Wall
from src.block.red_block import Red_Block
from src.block.blue_block import Blue_Block
from src.block.green_block import Green_Block
from src.block.floor import Floor
from src.item.bullet import Bullet
from src.item.ammo import Ammo
from src.bullet_display import BulletDisplay
from src.observer.goal import Goal
from src.ecs.components import AudioComponent
from src.ecs.systems import AudioSystem
from src.ecs.entities import Entity

pygame.init()

bullet_display = BulletDisplay()

# Initialize ECS Audio
audio_system = AudioSystem()

MUSIC_SOUND = pygame.mixer.Sound('assets/music/Gregoire Lourme - Commando Team (Action) [loop cut].ogg')
audio_entity = Entity("background_music")
audio_entity.add_component(AudioComponent(MUSIC_SOUND))
audio_system.process([audio_entity])

# Define colors
BG_COLOR = (153, 178, 178)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0,200,0)
BLUE = (0,0,200)
PINK = (255, 192, 203)

# Initialize Pygame
screen = pygame.display.set_mode((800, 665))
clock = pygame.time.Clock()

# Create entities
player = Player()
ammos = []
bullets = []
can_shoot = False

# Walls
walls = pygame.sprite.Group()
wall = Wall(0, 95, 50, 150) 

# Block
blocks = pygame.sprite.Group()

# Items
ammo_red = Ammo(RED, (432, 626))
ammo_green = Ammo(GREEN, (336, 338))
ammo_blue = Ammo(BLUE, (432, 50))

ammos.extend([ammo_red, ammo_green, ammo_blue])

# Create blocks and walls
def create_block_walls() :
    for i in range(screen.get_height() // wall.rect.height + 1):
        if i != 1 :
            wall1 = Wall(0, i * wall.rect.height, 50, 200)
            if i != 5 :
                if i != 3 and i != 4:
                    wall2 = Wall(96, i * wall.rect.height, 50, 200)
                    
                wall3 = Wall(192, i * wall.rect.height, 50, 200)
                if i != 3:
                    wall4 = Wall(288, i * wall.rect.height, 50, 200) 

        wall5 = Wall(480, i * wall.rect.height, 50, 200)

        walls.add(wall1, wall2, wall3, wall4, wall5)

        if i == 2 :
            block = Blue_Block(384, i * wall.rect.height, 50, 200)
            blocks.add(block)
        elif i == 4 :
            block = Red_Block(96, i * wall.rect.height, 50, 200)
            blocks.add(block)  
        elif i == 5 :
            block = Green_Block(384, i * wall.rect.height, 50, 200)
            blocks.add(block) 

create_block_walls()

# Floors
floors = pygame.sprite.Group()
floor = Floor(0, 96, 50, 200) 
num_rows = screen.get_height() // floor.rect.height + 1

for j in range(num_rows):
    for i in range(screen.get_width() // floor.rect.width - 2):
        floor_instance = Floor(i * floor.rect.width, j * floor.rect.height, 50, 200)
        floors.add(floor_instance)

# Font title
font_title = pygame.font.Font(None, 60)

# Font
font = pygame.font.Font(None, 36)

# Start
start_button = font.render("Start", True, BLACK)
start_button_rect = start_button.get_rect(center=(screen.get_width() // 2, 300))
start_button_rect.inflate_ip(40, 20)

# Quit
quit_button = font.render("Quit", True, BLACK)
quit_button_rect = quit_button.get_rect(center=(screen.get_width() // 2, 400))
quit_button_rect.inflate_ip(40, 20)

# Reset
reset_button = font.render("Reset", True, BLACK)
reset_button_rect = reset_button.get_rect(bottomright=(790 - 10, 655))

# Goal
goal = Goal(PINK,96,96*3,96,96)
goals = pygame.sprite.Group()
goals.add(goal)

def display_start_menu():
    screen.fill(BG_COLOR)
    title = font_title.render("Moon Tank", True, BLACK )
    screen.blit(title, (300,200))

    pygame.draw.rect(screen, (100, 50, 50), start_button_rect)
    text_rect = start_button.get_rect(center=start_button_rect.center)
    screen.blit(start_button, text_rect)


    pygame.draw.rect(screen, (50, 50, 100), quit_button_rect)
    text_rect = quit_button.get_rect(center=quit_button_rect.center)
    screen.blit(quit_button, text_rect)

    pygame.display.flip()

# Main game loop
def game_loop():
    global bullets
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:  
                    bullet = player.shoot(RED)
                    if bullet:
                        bullets.append(bullet)
                        bullet_display.decrement(bullet.color)
                elif event.key == pygame.K_x:  
                    bullet = player.shoot(GREEN)
                    if bullet:
                        bullets.append(bullet)
                        bullet_display.decrement(bullet.color)
                elif event.key == pygame.K_c:
                    bullet = player.shoot(BLUE)
                    if bullet:
                        bullets.append(bullet)
                        bullet_display.decrement(bullet.color)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if reset_button_rect.collidepoint(mouse_pos):
                    reset_game()

        # Check if the player reaches the goal
        if pygame.sprite.collide_rect(player, goal):
            goal.on_player_reach_goal()
            goal.display_popup(screen, "Congratulations! You reached the goal!")
            reset_game()


        # draw
        screen.fill(BG_COLOR)

        # groups of sprites can be drawn with group.draw()
        floors.draw(screen)
        walls.draw(screen)
        blocks.draw(screen)
        goals.draw(screen)

        # Add reset button
        pygame.draw.rect(screen, (50, 100, 50), reset_button_rect)
        text_rect = reset_button.get_rect(center=reset_button_rect.center)
        screen.blit(reset_button, text_rect)

        # Add goal 
        font = pygame.font.Font(None, 40)  
        text_surface = font.render("Goal", True, BLACK)  
        text_rect = text_surface.get_rect(center=(goal.rect.centerx, goal.rect.centery)) 
        screen.blit(text_surface, text_rect)

        # before player update
        previous_rect = player.rect.copy()

        # player update 
        player.update()

        # bullet update
        for bullet in bullets:
            bullet.update(walls, blocks)
            screen.blit(bullet.image, bullet.rect.topleft)
        bullets = [bullet for bullet in bullets if not bullet.should_remove]

        # check for collisions between player and walls
        wall_collisions = pygame.sprite.spritecollide(player, walls, False)
        for wall_collision in wall_collisions:
            if player.rect.right > wall_collision.rect.left and previous_rect.right <= wall_collision.rect.left:
                player.rect.right = wall_collision.rect.left
            # If the player is moving right, adjust its position to the left side of the wall
            elif player.rect.left < wall_collision.rect.right and previous_rect.left >= wall_collision.rect.right:
                player.rect.left = wall_collision.rect.right
            # If the player is moving up, adjust its position to the bottom side of the wall
            elif player.rect.bottom > wall_collision.rect.top and previous_rect.bottom <= wall_collision.rect.top:
                player.rect.bottom = wall_collision.rect.top
            # If the player is moving down, adjust its position to the top side of the wall
            elif player.rect.top < wall_collision.rect.bottom and previous_rect.top >= wall_collision.rect.bottom:
                player.rect.top = wall_collision.rect.bottom

        # check for collisions between player and blocks
        block_collisions = pygame.sprite.spritecollide(player, blocks, False)
        for block_collision in block_collisions:
            if player.rect.colliderect(block_collision.rect):
                if player.rect.right > block_collision.rect.left and previous_rect.right <= block_collision.rect.left:
                    player.rect.right = block_collision.rect.left
                elif player.rect.left < block_collision.rect.right and previous_rect.left >= block_collision.rect.right:
                    player.rect.left = block_collision.rect.right
                elif player.rect.bottom > block_collision.rect.top and previous_rect.bottom <= block_collision.rect.top:
                    player.rect.bottom = block_collision.rect.top
                elif player.rect.top < block_collision.rect.bottom and previous_rect.top >= block_collision.rect.bottom:
                    player.rect.top = block_collision.rect.bottom

        for ammo in ammos:
            if pygame.sprite.collide_rect(player, ammo):
                bullet_display.increment(ammo.color)
                player.collect(ammo.color)
                ammos.remove(ammo)

        # Display ammo image
        for ammo in ammos:
            screen.blit(ammo.image, ammo.rect.topleft)

        # Draw bullet display board
        bullet_display.draw(screen)

        # single sprites are drawn with screen.blit()
        screen.blit(player.image, (player.rect.x, player.rect.y))

        pygame.display.flip()
        clock.tick(30)

def main():
    display_start_menu()
    start_menu = True
    while start_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if start_button_rect.collidepoint(mouse_pos):
                    start_menu = False
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
        if not start_menu:
            game_loop()

# Reset all values
def reset_game():
    player.reset_position()

    walls.empty()
    blocks.empty()
    create_block_walls()

    ammos.clear()

    ammo_red = Ammo(RED, (432, 626))
    ammo_green = Ammo(GREEN, (336, 338))
    ammo_blue = Ammo(BLUE, (432, 50))
    ammos.extend([ammo_red, ammo_green, ammo_blue])

    bullet_display.reset()

# Run
if __name__ == "__main__":
    main()