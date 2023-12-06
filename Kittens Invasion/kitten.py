import pygame
from pygame.sprite import Sprite

class Kitten(Sprite):
    """A class to represent a single kitten."""

    def __init__(self, ki_game):
        """Initialise the kitten and set its starting position."""
        super().__init__()
        self.screen = ki_game.screen
        self.settings = ki_game.settings

        # Load the kitten image and set its rect attribute.
        self.image = pygame.image.load('images/angry_kitten.bmp')
        self.image = pygame.transform.scale(self.image, (96, 96))
        self.rect = self.image.get_rect()

        # Start each new kitten near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the kitten's exact horisontal position.
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Move the kitten to the right."""
        self.x += self.settings.kitten_speed * self.settings.squad_direction
        self.rect.x = self.x