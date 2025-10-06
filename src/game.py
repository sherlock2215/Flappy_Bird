import pygame
import sys
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    FPS,
    WHITE,
    SKY_BLUE,
    MENU,
    PLAYING,
    GAME_OVER,
    PIPE_FREQUENCY,
)
from bird import Bird
from pipe import Pipe


class FlappyBirdGame:
    """Main game class that manages the game state, objects, and loop."""

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Create game window
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()

        # Load assets
        self.background = pygame.image.load("../assets/images/background.png").convert()
        self.ground = pygame.image.load("../assets/images/ground.png").convert()
        self.ground_rect = self.ground.get_rect(topleft=(0, SCREEN_HEIGHT - 100))

        # Game objects
        self.bird = Bird(self.screen)
        self.pipes = []

        # Game state
        self.game_state = MENU
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 30)

        # Timers
        self.pipe_timer = 0

    def handle_events(self):
        """Handle all game events like keyboard input and quitting."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.game_state == MENU:
                        self.start_game()
                    elif self.game_state == PLAYING:
                        self.bird.flap()
                    elif self.game_state == GAME_OVER:
                        self.reset_game()

    def start_game(self):
        """Start a new game from the menu."""
        self.game_state = PLAYING
        self.score = 0
        self.pipes = []
        self.bird = Bird(self.screen)

    def reset_game(self):
        """Reset the game after game over."""
        self.game_state = MENU
        self.score = 0
        self.pipes = []
        self.bird = Bird(self.screen)

    def spawn_pipes(self):
        """Spawn new pipes at regular intervals."""
        current_time = pygame.time.get_ticks()
        if current_time - self.pipe_timer > PIPE_FREQUENCY:
            self.pipes.append(Pipe())
            self.pipe_timer = current_time

    def update_pipes(self):
        """Update all pipes and handle scoring."""
        for pipe in self.pipes[:]:
            pipe.update()

            # Check for scoring
            if pipe.check_score(self.bird.rect):
                self.score += 1

            # Remove off-screen pipes
            if pipe.is_off_screen():
                self.pipes.remove(pipe)

    def check_collisions(self):
        """Check for collisions between bird and pipes/ground."""
        return self.bird.check_collision(self.pipes, self.ground_rect.top)

    def draw_background(self):
        """Draw the background and ground."""
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.ground, self.ground_rect)

    def draw_ui(self):
        """Draw the score and game over text."""
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        if self.game_state == MENU:
            menu_text = self.font.render("Press SPACE to start", True, WHITE)
            self.screen.blit(menu_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2))
        elif self.game_state == GAME_OVER:
            game_over_text = self.font.render("Game Over! Press SPACE", True, WHITE)
            self.screen.blit(
                game_over_text, (SCREEN_WIDTH // 2 - 120, SCREEN_HEIGHT // 2)
            )

    def update(self):
        """Update game logic based on current state."""
        if self.game_state == PLAYING:
            # Update bird
            self.bird.update()
            self.bird.animate()

            # Handle pipes
            self.spawn_pipes()
            self.update_pipes()

            # Check for collisions
            if self.check_collisions():
                self.game_state = GAME_OVER

    def draw(self):
        """Draw all game elements."""
        self.draw_background()

        # Draw pipes
        for pipe in self.pipes:
            pipe.draw(self.screen)

        # Draw bird
        self.bird.draw()

        # Draw UI
        self.draw_ui()

    def run(self):
        """Main game loop."""
        while True:
            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(FPS)
