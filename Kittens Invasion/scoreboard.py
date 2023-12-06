import pygame.font
from pygame.sprite import Group
from fish_plate import FishPlate

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ki_game):
        self.ki_game = ki_game
        self.screen = ki_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ki_game.settings
        self.stats = ki_game.stats

        # Font settings for scoring information.
        self.text_color = (100, 100, 100)
        self.font = pygame.font.SysFont(None, 40)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_fish_plates()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}".replace(",", " ")
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top left of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"Highest score: {high_score:,}".replace(",", " ")
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = "Level " + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        # Position the level at the top left of the screen.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.top

    def prep_fish_plates(self):
        """Show how many plates are left."""
        self.fish_plates = Group()
        for fish_plate_number in range(self.stats.fish_plates_left):
            fish_plate = FishPlate(self.ki_game)
            fish_plate.image = pygame.transform.scale(fish_plate.image, (40, 40))
            fish_plate.rect.x = 20 + fish_plate_number * (fish_plate.image.get_rect().width + 10)
            fish_plate.rect.y = self.score_rect.height + 30
            self.fish_plates.add(fish_plate)

    def show_score(self):
        """Draw scores and level to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.fish_plates.draw(self.screen)

    def check_high_score(self):
        """Chech to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()