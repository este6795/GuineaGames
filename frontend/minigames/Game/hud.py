
### FIX ME ###
# We need to implement a method that loads fruits or coins into the maze
# for the player to collect as they navigate through it.

### FIX ME ###
# We need to somehow handle scoring and display it on the HUD
# as the player collects items in the maze


### FIX ME ###
    # We need to somehow display a game over screen when the player loses

### FIX ME ###
    # We need to somehow display a you win screen when the player loses

import pygame
import os
from settings import FONT_NAME, FONT_SIZE, WHITE

# HUD asset path (if needed in future)
base_path = os.path.dirname(__file__)
assets_path = os.path.join(base_path, ".../Global Assets/Game Sprites/Mini-game/images/hud")

class HUD:
    def __init__(self):
        self.font = pygame.font.Font(FONT_NAME, FONT_SIZE)

    def draw(self, screen, score, lives):
        """Draw the HUD on the given screen."""
        score_text = self.font.render(f"Score: {score}", True, WHITE)
        lives_text = self.font.render(f"Lives: {lives}", True, WHITE)

        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 40))