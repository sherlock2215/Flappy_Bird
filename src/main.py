#!/usr/bin/env python3
"""
Flappy Bird - Main Entry Point
A Python implementation of the classic Flappy Bird game using Pygame.
"""

from game import FlappyBirdGame


def main():
    """Initialize and run the Flappy Bird game."""
    try:
        game = FlappyBirdGame()
        game.run()
    except Exception as e:
        print(f"Error starting the game: {e}")
        print("Please make sure all asset files are in the correct location.")


if __name__ == "__main__":
    main()
