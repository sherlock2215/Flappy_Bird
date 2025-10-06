"""
Game configuration constants for Flappy Bird.
Centralizes all game settings for easy modification.
"""

# Game window settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# Physics and game mechanics
GRAVITY = 0.25
FLAP_STRENGTH = -7
PIPE_SPEED = 3
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds

# Bird settings
BIRD_START_X = 50
BIRD_START_Y = 300

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
SKY_BLUE = (135, 206, 235)

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2
