### FIX ME ###
    # We need to implement an enemy that chases the player around the maze
    # and causes the player to lose if they come into contact with it.
import pygame
import random
import os
from settings import TILE_SIZE, GOLD
from maze_generator import MazeGenerator
from asset_loader import load_image
class Enemy:
    def __init__(self, pos_x=0, pos_y=0, color=GOLD, seed=None, speed=500):
        """Create an enemy. If file_path is None, use the repository assets_dir.

        file_path may be either a directory containing the image or a direct
        path to an image file.
        """
        self.position = [pos_x, pos_y]
        self.color = color
        self.seed = seed
        self.speed = speed
        self.last_move_time = 0 # Time of the last move in milliseconds
#       self.loaded_image = load_image("enemy/MG_Dragon.png", TILE_SIZE)
#        self.image = pygame.transform.scale(self.loaded_image, (TILE_SIZE, TILE_SIZE))
    
    def can_move(self):
        """Determine if the enemy can move based on speed and time."""
        now = pygame.time.get_ticks()
        return now - self.last_move_time >= self.speed

    def move_towards_player(self, player_pos, maze):
        """Move the enemy one step towards the player if possible."""
        # Simple logic to move towards the player
        if not self.can_move():
            return


        ### FIX ME ###
        # At the moment, the enemy just moves directly towards the player, however this should be more random
        if self.position[0] < player_pos[0] and maze.is_wall(self.position[0] + 1, self.position[1]) == False:
            self.position[0] += 1
            self.last_move_time = pygame.time.get_ticks()
        elif self.position[0] > player_pos[0] and maze.is_wall(self.position[0] - 1, self.position[1]) == False:
            self.position[0] -= 1
            self.last_move_time = pygame.time.get_ticks()
        elif self.position[1] < player_pos[1] and maze.is_wall(self.position[0], self.position[1] + 1) == False:
            self.position[1] += 1
            self.last_move_time = pygame.time.get_ticks()
        elif self.position[1] > player_pos[1] and maze.is_wall(self.position[0], self.position[1] - 1) == False:
            self.position[1] -= 1
            self.last_move_time = pygame.time.get_ticks()
    
    def add_enemies(self, grid):
        """Randomly add enemies ('E') to the maze."""
        if self.seed is not None:
            random.seed(self.seed)
        
        # Find all spawn points
        spawn_points = []
        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                if tile == 'S':
                    spawn_points.append((x, y))
        
        # If there are spawn points, randomly select one for the enemy
        new_grid = [list(row) for row in grid]  # Convert strings to lists for easier modification
        if spawn_points:
            enemy_x, enemy_y = random.choice(spawn_points)
            new_grid[enemy_y][enemy_x] = 'E'
            self.position = [enemy_x, enemy_y]
        
        # Convert back to strings
        return [''.join(row) for row in new_grid]
    
    def enemy_pos(self):
        return (self.position[0], self.position[1])

    def draw(self, screen):
        """Draw the enemy on the given screen."""
        rect = pygame.Rect(self.position[0] * TILE_SIZE, self.position[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, self.color, rect)
#        screen.blit(self.image, (self.position[0] * TILE_SIZE, self.position[1] * TILE_SIZE))
    