import os 
import pygame 

### FIX ME ###
# This file should handle loading assets such as images, sounds, and fonts from the Global Assets directory, however, seems to not be doing that currently.


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "Global Assets", "Game Sprites", "Mini-game")
PIG_ASSETS_DIR = os.path.join(BASE_DIR, "Global Assets", "Game Sprites", "Guinea Pigs")

def load_image(name, scale=None):
    """Load an image from the assets directory. Optionally scale it."""
    path = os.path.join(ASSETS_DIR, "images" ,name)
    try:
        image = pygame.image.load(path).convert_alpha()
        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except Exception as e:
        print(f"Error loading image {name}: {e}")
        return None

def load_guinea_image(name, scale=None):
    """Load a guinea pig image from the assets directory. Optionally scale it."""
    path = os.path.join(PIG_ASSETS_DIR, "LH_GP_Sprites", name)
    try:
        image = pygame.image.load(path).convert_alpha()
        if scale:
            image = pygame.transform.scale(image, scale)
        return image
    except Exception as e:
        print(f"Error loading guinea pig image {name}: {e}")
        return None

def load_sound(name):
    """Load a sound from the assets directory."""
    path = os.path.join(ASSETS_DIR, "audio", name)
    try:
        sound = pygame.mixer.Sound(path)
        return sound
    except Exception as e:
        print(f"Error loading sound {name}: {e}")
        return None

def load_font(name, size):
    """Load a font from the assets directory."""
    path = os.path.join(ASSETS_DIR, "fonts", name)
    try:
        font = pygame.font.Font(path, size)
        return font
    except Exception as e:
        print(f"Error loading font {name}: {e}")
        return None