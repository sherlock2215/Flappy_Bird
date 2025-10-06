import pygame
from config import GRAVITY, FLAP_STRENGTH, BIRD_START_X, BIRD_START_Y

class Bird:
    """Represents the player-controlled bird in the game."""
    
    def __init__(self, screen, image_path="assets/images/bird.png"):
        self.screen = screen
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=(BIRD_START_X, BIRD_START_Y))
        self.movement = 0
        self.alive = True
    
    def flap(self):
        """Make the bird jump upwards."""
        self.movement = FLAP_STRENGTH
    
    def update(self):
        """Update the bird's position and physics."""
        # Apply gravity
        self.movement += GRAVITY
        self.rect.centery += self.movement
        
        # Prevent bird from going above the screen
        if self.rect.top <= 0:
            self.rect.top = 0
            self.movement = 0
    
    def draw(self):
        """Draw the bird on the screen."""
        self.screen.blit(self.image, self.rect)
    
    def check_collision(self, pipes, ground_height):
        """Check for collisions with pipes or ground."""
        # Check ground collision
        if self.rect.bottom >= ground_height:
            self.alive = False
            return True
        
        # Check pipe collisions
        for pipe in pipes:
            if self.rect.colliderect(pipe.rect):
                self.alive = False
                return True
        
        return False
