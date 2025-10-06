import pygame
from config import GRAVITY, FLAP_STRENGTH, BIRD_START_X, BIRD_START_Y


class Bird:
    """Represents the player-controlled bird in the game."""

    def __init__(self, screen):
        self.screen = screen
        # Use YOUR actual bird images
        self.frames = [
            pygame.image.load("../assets/images/bird1.png").convert_alpha(),
            pygame.image.load("../assets/images/bird2.png").convert_alpha(),
            pygame.image.load("../assets/images/bird3.png").convert_alpha()
        ]
        self.frame_index = 0
        self.image = self.frames[self.frame_index]
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
    def animate(self):
        """Cycle through bird frames for flapping animation."""
        self.frame_index = (self.frame_index + 0.1) % len(self.frames)
        self.image = self.frames[int(self.frame_index)]

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
