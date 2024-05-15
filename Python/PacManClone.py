import pygame
import sys
import random
import time
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
PACMAN_SIZE = 30
PELLET_SIZE = 10
ENEMY_SIZE = 20
PACMAN_COLOR = (255, 255, 0)
PELLET_COLOR = (255, 255, 255)
ENEMY_COLOR = (255, 0, 0)
FPS = 60

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Clone")

# Set up the clock
clock = pygame.time.Clock()

# Pac-Man initial position
pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2

# Pac-Man velocity
pacman_speed = 5
pacman_direction = 0  # 0: right, 1: down, 2: left, 3: up

# Pellets
level_pellets = 10
pellets = [(random.randint(0, WIDTH - PELLET_SIZE), random.randint(0, HEIGHT - PELLET_SIZE)) for _ in range(level_pellets)]

# Enemies
num_enemies = 3
enemies = [(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(0, HEIGHT - ENEMY_SIZE), pacman_speed // 2)
           for _ in range(num_enemies)]

# Game variables
level = 1
score = 0
lives = 3
start_time = time.time()

# Function to reset game elements for a new level
def reset_game_elements():
    global pacman_x, pacman_y, pacman_direction, pellets, enemies
    pacman_x = WIDTH // 2
    pacman_y = HEIGHT // 2
    pacman_direction = 0
    pellets = [(random.randint(0, WIDTH - PELLET_SIZE), random.randint(0, HEIGHT - PELLET_SIZE)) for _ in range(level_pellets)]
    enemies = [(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(0, HEIGHT - ENEMY_SIZE), pacman_speed // 2)
               for _ in range(num_enemies)]

# Function to calculate the angle between two points
def calculate_angle(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)

# Game loop
# Check for adding lives when reaching pointsreq
pointsreq = 25  # Set the initial points requirement

while lives > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        pacman_direction = 0
    elif keys[pygame.K_DOWN]:
        pacman_direction = 1
    elif keys[pygame.K_LEFT]:
        pacman_direction = 2
    elif keys[pygame.K_UP]:
        pacman_direction = 3

    # Move Pac-Man
    if pacman_direction == 0:
        pacman_x = (pacman_x + pacman_speed) % WIDTH
    elif pacman_direction == 1:
        pacman_y = (pacman_y + pacman_speed) % HEIGHT
    elif pacman_direction == 2:
        pacman_x = (pacman_x - pacman_speed) % WIDTH
    elif pacman_direction == 3:
        pacman_y = (pacman_y - pacman_speed) % HEIGHT

    # Move Enemies towards Pac-Man
    for i, enemy in enumerate(enemies):
        enemy_x, enemy_y, enemy_speed = enemy

        # Calculate angle between enemy and Pac-Man
        angle = calculate_angle(enemy_x, enemy_y, pacman_x, pacman_y)

        # Update enemy position based on angle
        enemy_x += math.cos(angle) * enemy_speed
        enemy_y += math.sin(angle) * enemy_speed

        enemies[i] = (enemy_x, enemy_y, enemy_speed)  # Update enemy position in the list

        # Check for collision with Pac-Man
        enemy_rect = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)
        pacman_rect = pygame.Rect(pacman_x - PACMAN_SIZE // 2, pacman_y - PACMAN_SIZE // 2, PACMAN_SIZE, PACMAN_SIZE)

        if enemy_rect.colliderect(pacman_rect):
            lives -= 1
            reset_game_elements()

    # Check for pellet collisions
    collected_pellets = []
    for pellet in pellets:
        pellet_rect = pygame.Rect(pellet[0], pellet[1], PELLET_SIZE, PELLET_SIZE)
        pacman_rect = pygame.Rect(pacman_x - PACMAN_SIZE // 2, pacman_y - PACMAN_SIZE // 2, PACMAN_SIZE, PACMAN_SIZE)

        if pellet_rect.colliderect(pacman_rect):
            collected_pellets.append(pellet)

    # Remove collected pellets
    for pellet in collected_pellets:
        pellets.remove(pellet)
        score += 1

    # Draw background
    screen.fill((0, 0, 0))

    # Draw Pellets
    for pellet in pellets:
        pygame.draw.circle(screen, PELLET_COLOR, (pellet[0] + PELLET_SIZE // 2, pellet[1] + PELLET_SIZE // 2),
                           PELLET_SIZE // 2)

    # Draw Enemies
    for enemy in enemies:
        pygame.draw.rect(screen, ENEMY_COLOR, (enemy[0], enemy[1], ENEMY_SIZE, ENEMY_SIZE))

    # Draw Pac-Man
    pygame.draw.circle(screen, PACMAN_COLOR, (int(pacman_x), int(pacman_y)), PACMAN_SIZE // 2)

    # Draw Score, Level, and Lives
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH // 2 - level_text.get_width() // 2, 10))
    screen.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))

    # Check if all pellets are collected and update level
    if not pellets:
        level += 1
        level_pellets += 5
        pellets = [(random.randint(0, WIDTH - PELLET_SIZE), random.randint(0, HEIGHT - PELLET_SIZE))
                   for _ in range(level_pellets)]
        reset_game_elements()

    # Check for adding lives when reaching pointsreq
    if score >= pointsreq:
        lives += 1
        pointsreq = (pointsreq * 2)  # Update points requirement for the next extra life
        # You can adjust this multiplier as needed

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Game over
pygame.quit()
sys.exit()
