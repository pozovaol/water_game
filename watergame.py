import pygame
import random

# Initialize Pygame
pygame.init()

import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Water Game")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Set up the player (water droplet)
droplet_radius = 10
droplet_x = window_width // 2
droplet_y = window_height - droplet_radius * 2
droplet_speed = 5

# Set up the raindrop
raindrop_radius = 5
raindrop_x = random.randint(0, window_width - raindrop_radius)
raindrop_y = 0
raindrop_speed = 3

# Game loop
running = True
clock = pygame.time.Clock()

score = 0
font = pygame.font.Font(None, 36)

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the droplet
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        droplet_x -= droplet_speed
    if keys[pygame.K_RIGHT]:
        droplet_x += droplet_speed

    # Move the raindrop
    raindrop_y += raindrop_speed

    # Check for collision
    if (
        raindrop_y + raindrop_radius >= droplet_y
        and raindrop_y <= droplet_y + droplet_radius * 2
        and raindrop_x + raindrop_radius >= droplet_x
        and raindrop_x <= droplet_x + droplet_radius * 2
    ):
        score += 1
        raindrop_x = random.randint(0, window_width - raindrop_radius)
        raindrop_y = 0

    # Check if raindrop reached the bottom
    if raindrop_y >= window_height:
        raindrop_x = random.randint(0, window_width - raindrop_radius)
        raindrop_y = 0

    # Clear the window
    window.fill(WHITE)

    # Draw the droplet
    pygame.draw.circle(window, BLUE, (droplet_x, droplet_y), droplet_radius)

    # Draw the raindrop
    pygame.draw.circle(window, BLUE, (raindrop_x, raindrop_y), raindrop_radius)

    # Display the score
    score_text = font.render("Score: " + str(score), True, BLUE)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Limit frames per second
    clock.tick(60)

# Quit the game
pygame.quit()