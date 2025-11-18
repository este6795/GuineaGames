
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
from settings import WHITE, RED, GREEN

class HUD:
    def __init__(self, player):
        self.player = player
        self.font = pygame.font.SysFont("Arial", 24)
        self.bar_width = 200
        self.bar_height = 20
        self.margin = 10
        self.score = 0

    def draw_score(self, screen): 
        text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(text, (450 ,self.margin))

    def draw_win(self, screen):
        pass

    def draw_lose(self, screen):
        pass

    def draw_stamina_bar(self, screen):
        x = self.margin 
        y = self.margin

        # Outline of stamina bar
        pygame.draw.rect(screen, WHITE, (x, y, self.bar_width, self.bar_height), 2)

        # Filling Amount
        stamina_ratio = self.player.stamina / self.player.stamina_max
        fill_width = int(self.bar_width * stamina_ratio)
        
        # Bar color
        color = GREEN if self.player.is_boosting else RED 

        pygame.draw.rect(screen, color, (x, y, fill_width, self.bar_height))

    def draw(self, screen):
        self.draw_stamina_bar(screen)
        self.draw_score(screen)


