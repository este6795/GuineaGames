import pygame
from guineapig import Guineapig

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Image Display Example")

# --- THIS IS WHERE YOU SHOULD LOAD ASSETS ---
try:
    # Load the image ONCE here, before the loop
    image = pygame.image.load('images/guineapig.png') 
    player_pig = Guineapig(screen_width // 2, screen_height // 2)
except pygame.error as message:
    print(f"Cannot load image: {message}")
    pygame.quit()
    exit()

# Get the image rectangle for positioning
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)  # Center the image
# --- END OF ASSET LOADING ---



# --- THIS IS YOUR "MAIN" LOOP ---
running = True
while running:
    # 1. Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update Game Logic (nothing to update yet)
    # ...

    # 3. Draw to Screen
    screen.fill((255, 255, 255))  # White background
    screen.blit(image, image_rect) # Draw the image

    # 4. Update the Display
    pygame.display.flip() # <--- THIS MUST BE INSIDE THE LOOP

# Quit Pygame
pygame.quit()