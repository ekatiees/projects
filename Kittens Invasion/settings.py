class Settings:
    """A class to store all settings for Kittens Invasion."""

    def __init__(self):
        """Initialise the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Fish plate settings
        self.fish_plate_limit = 3

        # Flying fish settings
        self.fish_flys_allowed = 3

        # Kitten settings
        self.squad_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 2
        # How quicklythe kitten points values increase
        self.score_scale = 1.5

        self.initialise_dynamic_settings()

    def initialise_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.fish_plate_speed = 4.0
        self.fish_fly_speed = 2.5
        self.kitten_speed = 1.0

        # squad_directoin of 1 represents right; -1 represents left.
        self.squad_direction = 1

        # Scoring settings
        self.kitten_points = 50

    def increase_speed(self):
        """Increase speen settings and kitten point values."""
        self.fish_plate_speed *= self.speedup_scale
        self.fish_fly_speed *= self.speedup_scale
        self.kitten_speed *= self.speedup_scale

        self.kitten_points = int(self.kitten_points * self.score_scale)