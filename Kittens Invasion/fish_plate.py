import pygame
from pygame.sprite import Sprite

class FishPlate(Sprite):
    """A class to manage the fish plate."""

    def __init__(self, ki_game):
        """Initialise the fish plate and set its starting position."""
        super().__init__()
        self.screen = ki_game.screen
        self.settings = ki_game.settings
        self.screen_rect = ki_game.screen.get_rect()

        # Load the fish plate image and get its rect.
        self.image = pygame.image.load('images/fish_plate.bmp')
        self.rect = self.image.get_rect()

        # Start each new fish plate at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the fish plate's exact horisontal position.
        self.x = float(self.rect.x)

        # Movement flag; start with a fish plate that's not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the fish plate's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.fish_plate_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.fish_plate_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the fish plate at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_fish_plate(self):
        """Center the fish plate on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)