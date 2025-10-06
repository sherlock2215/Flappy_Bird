import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PIPE_GAP, PIPE_SPEED

class Pipe:
    """Represents a pair of pipes (top and bottom) that the bird must navigate through."""
    
    def __init__(self, image_path="assets/images/pipe.png"):
        self.image = pygame.image.load(image_path).convert_alpha()
        
        # Create top pipe (flipped)
        self.top_pipe = pygame.transform.flip(self.image, False, True)
        self.top_rect = self.top_pipe.get_rect()
        
        # Create bottom pipe
        self.bottom_pipe = self.image
        self.bottom_rect = self.bottom_pipe.get_rect()
        
        # Set initial positions
        self._reset_position()
        self.passed = False  # Track if bird has passed this pipe
    
    def _reset_position(self):
        """Set the pipe to a new random position at the right side of screen."""
        pipe_height = random.randint(150, 400)
        
        # Position top pipe
        self.top_rect.bottomleft = (SCREEN_WIDTH, pipe_height - PIPE_GAP // 2)
        
        # Position bottom pipe  
        self.bottom_rect.topleft = (SCREEN_WIDTH, pipe_height + PIPE_GAP // 2)
    
    def update(self):
        """Move the pipes to the left."""
        self.top_rect.x -= PIPE_SPEED
        self.bottom_rect.x -= PIPE_SPEED
    
    def draw(self, screen):
        """Draw both pipes on the screen."""
        screen.blit(self.top_pipe, self.top_rect)
        screen.blit(self.bottom_pipe, self.bottom_rect)
    
    def is_off_screen(self):
        """Check if the pipes have moved completely off the left side of screen."""
        return self.top_rect.right < 0
    
    def check_collision(self, bird_rect):
        """Check if the bird collides with either pipe."""
        return bird_rect.colliderect(self.top_rect) or bird_rect.colliderect(self.bottom_rect)
    
    def check_score(self, bird_rect):
        """Check if bird has passed the pipes to score a point."""
        if not self.passed and self.top_rect.right < bird_rect.left:
            self.passed = True
            return True
        return False
