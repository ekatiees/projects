class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ki_game):
        """Initialise statistics."""
        self.settings = ki_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.fish_plates_left = self.settings.fish_plate_limit
        self.score = 0
        self.level = 1