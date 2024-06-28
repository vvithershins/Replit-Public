#This file was entirely AI generated
import pygame
import random
import string

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Balloon Popping Typing Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)

# Balloon class
class Balloon:
    def __init__(self):
        self.x = random.randint(50, WIDTH - 50)
        self.y = HEIGHT
        self.speed = random.randint(1, 3)
        self.letter = random.choice(string.ascii_lowercase)
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.radius = 30

    def move(self):
        self.y -= self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, int(self.y)), self.radius)
        text = font.render(self.letter, True, BLACK)
        text_rect = text.get_rect(center=(self.x, int(self.y)))
        screen.blit(text, text_rect)

# Game variables
balloons = []
score = 0
game_over = False

# Game loop
clock = pygame.time.Clock()
balloon_spawn_time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if not game_over:
                for balloon in balloons:
                    if event.unicode.lower() == balloon.letter:
                        balloons.remove(balloon)
                        score += 1
                        break

    if not game_over:
        # Spawn new balloons
        current_time = pygame.time.get_ticks()
        if current_time - balloon_spawn_time > 2000:  # Spawn every 2 seconds
            balloons.append(Balloon())           
            balloon_spawn_time = current_time

        # Move balloons
        for balloon in balloons:
            balloon.move()
            if balloon.y < 0:
                game_over = True

    # Draw everything
    screen.fill(WHITE)

    for balloon in balloons:
        balloon.draw(screen)

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    if game_over:
        game_over_text = font.render("Game Over!", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 70, HEIGHT // 2 - 18))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
