import pygame
from pygame.sprite import Sprite

class FishFly(Sprite):
    """A class to manage flying fish sent from the fish plate."""

    def __init__(self, ki_game):
        """Create a flying fish object at the fish plate's current position."""
        super().__init__()
        self.screen = ki_game.screen
        self.settings = ki_game.settings
        
        # Load the fish plate image and get its rect.
        self.image = pygame.image.load('images/fish_fly.bmp')
        self.image = pygame.transform.scale(self.image, (35.3, 77))
        self.rect = self.image.get_rect()

        # Set correct position.
        self.rect.midtop = ki_game.fish_plate.rect.midtop

        # Store the flying fish's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the flying fish up the screen."""
        # Update the exact position of the flying fish.
        self.y -= self.settings.fish_fly_speed
        # Update the rect position.
        self.rect.y = self.y

    def blitme(self):
        """Draw the flying fish to the screen."""
        self.screen.blit(self.image, self.rect)