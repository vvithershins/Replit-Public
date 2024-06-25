import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Frogger")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
brown = (165, 42, 42)

# Frog properties
frog_size = 20
frog_x = screen_width // 2 - frog_size // 2
frog_y = screen_height - frog_size
frog_speed = 10

# Log properties
log_width = 60
log_height = 20
log_speed = 2
logs = []
num_logs = 5

# Car properties
car_width = 40
car_height = 20
car_speed = 4
cars = []
num_cars = 5

# Create logs
for i in range(num_logs):
    log_x = random.randint(0, screen_width - log_width)
    log_y = random.randint(screen_height // 2 - 100, screen_height // 2)
    logs.append([log_x, log_y])

# Create cars
for i in range(num_cars):
    car_x = random.randint(0, screen_width - car_width)
    car_y = random.randint(0, screen_height // 2)
    cars.append([car_x, car_y])

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                frog_x -= frog_speed
            elif event.key == pygame.K_RIGHT:
                frog_x += frog_speed
            elif event.key == pygame.K_UP:
                frog_y -= frog_speed
            elif event.key == pygame.K_DOWN:
                frog_y += frog_speed

    # Keep frog within screen bounds
    if frog_x < 0:
        frog_x = 0
    elif frog_x > screen_width - frog_size:
        frog_x = screen_width - frog_size
    if frog_y < 0:
        frog_y = 0
    elif frog_y > screen_height - frog_size:
        frog_y = screen_height - frog_size

    # Move logs
    for log in logs:
        log[0] -= log_speed
        if log[0] < -log_width:
            log[0] = screen_width
    # Move cars
    for car in cars:
        car[0] += car_speed
        if car[0] > screen_width:
            car[0] = -car_width

    # Check for collisions with cars
    for car in cars:
        if frog_x < car[0] + car_width and frog_x + frog_size > car[0] and \
           frog_y < car[1] + car_height and frog_y + frog_size > car[1]:
            print("Game Over!")
            running = False

    # Check for collisions with logs
    for log in logs:
        if frog_x < log[0] + log_width and frog_x + frog_size > log[0] and \
           frog_y < log[1] + log_height and frog_y + frog_size > log[1]:
            frog_x -= log_speed
            if frog_x < 0:
                frog_x = 0
            elif frog_x > screen_width - frog_size:
                frog_x = screen_width - frog_size

    # Draw everything
    screen.fill(green)  # Draw grass
    for log in logs:
        pygame.draw.rect(screen, brown, (log[0], log[1], log_width, log_height))
    for car in cars:
        pygame.draw.rect(screen, black, (car[0], car[1], car_width, car_height))
    pygame.draw.rect(screen, white, (frog_x, frog_y, frog_size, frog_size))  # Draw frog

    pygame.display.flip()
    pygame.time.Clock().tick(30)  # Limit to 30 frames per second

pygame.quit()
