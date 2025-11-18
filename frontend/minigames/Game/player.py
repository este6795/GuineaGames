import pygame 
import random
import os
from settings import TILE_SIZE, RED

class Player:
    def __init__(self, x=0, y=0, color=RED, seed=None, speed=3, stamina=3):
        # Player position
        self.pos_x = x
        self.pos_y = y

        # Player appearance
        self.color = color

        # Random seed for reproducibility
        self.seed = seed
       
        # Speed related attributes
        self.base_speed = 1
        self.boosted_speed = speed
        self.speed_level = 1

        #Cooldown system
        self.BASE_COOLDOWN = 500 # Base cooldown in milliseconds
        self.SPEED_STEP = 45 # Base cooldown step in milliseconds
        self.move_cooldown = self._calc_cooldown(self.speed_level)
        self.last_move_time = 0 # Time of the last move in milliseconds

        # Stamina/Endurance System (Should transition to levels rather than milliseconds)
        self.stamina = 0
        self.stamina_max = 100
        self.stamina_level = stamina 

        self.stamina_gain = 3 * self.stamina_level
        self.stamina_drain = 20 - (2 * self.stamina_level)
        self.boost_threashold = 100 - (5 * self.stamina_level)
        self.is_boosting = False 

    def can_move(self):
        """Determine if the player can move based on speed and time."""
        now = pygame.time.get_ticks()
        return now - self.last_move_time >= self.move_cooldown

    def _calc_cooldown(self, speed_level):
        return self.BASE_COOLDOWN - (speed_level * self.SPEED_STEP)
    
    def updated_stamina(self): 
        # print(f'Current speed is: {self.stamina}')
        now = pygame.time.get_ticks()

        if self.is_boosting: 
            drain_amount = self.stamina_drain * ((now - self.last_move_time) / 100)
            # print(f'Draining by: {drain_amount}')
            self.stamina -= drain_amount
            if self.stamina <= 0: 
                self.stamina = 0
                self.is_boosting = False 
                self.speed_level = self.base_speed 
                self.move_cooldown = self._calc_cooldown(self.speed_level)

        else: 
            if self.stamina >= self.boost_threashold:
                self.is_boosting = True
                self.speed_level = self.boosted_speed
                self.move_cooldown = self._calc_cooldown(self.speed_level)
   
    def move(self, dx, dy, maze):
        """Move the player by (dx, dy) if the target position is not a wall."""

        if not self.can_move():
            return

        new_x = self.pos_x + dx
        new_y = self.pos_y + dy

        # Only move when the destination is not a wall
        if not maze.is_wall(new_x, new_y):
            self.pos_x = new_x
            self.pos_y = new_y

            # Gain stamina as player moves
            self.stamina += self.stamina_gain
            if self.stamina > self.stamina_max: 
                self.stamina = self.stamina_max
            
            # Update stamina/boost logic
            self.updated_stamina()

            self.last_move_time = pygame.time.get_ticks() # Update last move time

    def add_player(self, grid):
        """Randomly add player ('P') to the maze."""
        if self.seed is not None:
            random.seed(self.seed)
        
        # Find all spawn points
        spawn_points = []
        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                if tile == '0':
                    spawn_points.append((x, y))
        
        # If there are spawn points, randomly select one for the player
        new_grid = [list(row) for row in grid]  # Convert strings to lists for easier modification
        if spawn_points:
            player_x, player_y = random.choice(spawn_points)
            new_grid[player_y][player_x] = 'P'
            # Update this Player instance so its coordinates match the placed 'P'
            self.pos_x = player_x
            self.pos_y = player_y
        
        # Convert back to strings
        return [''.join(row) for row in new_grid]

    def player_pos(self):
        return (self.pos_x, self.pos_y)

    def draw(self, screen):
        """Draw the player on the given screen."""
        rect = pygame.Rect(self.pos_x * TILE_SIZE, self.pos_y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, self.color, rect)