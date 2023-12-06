import sys
from time import sleep
import pygame
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from fish_plate import FishPlate
from fish_fly import FishFly
from kitten import Kitten

class KittensInvasion:
    """Overall class to manage game assets and behaviour."""
    
    def __init__(self):
        """Initialise the game, and create game resources."""
        pygame.init()

        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Kittens Invasion")

        # Create an instance to store game statistics,
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.fish_plate = FishPlate(self)
        self.fish_flys = pygame.sprite.Group()
        self.kittens = pygame.sprite.Group()

        self._create_squad()

        # Start Kittens Invasion in an active state.
        self.game_active = False

        # Make the Play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.fish_plate.update()
                self._update_fish_flys()
                self._update_kittens()
                
            self._update_screen()
            self.clock.tick(60) # FPS = 60
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game settings.
            self.settings.initialise_dynamic_settings()
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_fish_plates()
            self.game_active = True

            # Get rid of any remaining flying fish and kittens.
            self.fish_flys.empty()
            self.kittens.empty()

            # Create a new squad and center the plate.
            self._create_squad()
            self.fish_plate.center_fish_plate()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.fish_plate.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.fish_plate.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_fish()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.fish_plate.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.fish_plate.moving_left = False
    
    def _fire_fish(self):
        """Create a new flying fish and add it io the fish group (fish_flys)"""
        if len(self.fish_flys) < self.settings.fish_flys_allowed:
            new_fish = FishFly(self)
            self.fish_flys.add(new_fish)
    
    def _update_fish_flys(self):
        """Update position of flying fish and get rid of old ones."""
        self.fish_flys.update()

        # Get rid of fish that have disappeared.
        for fish in self.fish_flys.copy():
            if fish.rect.bottom <= 0:
                self.fish_flys.remove(fish)
        
        self._check_fish_kitten_collisions()

    def _check_fish_kitten_collisions(self):
        """Respond to fish-kitten collisions."""
        # Remove any fish and kittens that have collided.
        collisions = pygame.sprite.groupcollide(self.fish_flys, self.kittens, True, True)

        if collisions:
            for kittens in collisions.values():
                self.stats.score += self.settings.kitten_points * len(kittens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.kittens:
            # Remove existing flying fish and create new kitten squad.
            self.fish_flys.empty()
            self._create_squad()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()
    
    def _fish_plate_hit(self):
        """Respond to the fish plate being hit my a kitten."""
        if self.stats.fish_plates_left > 0:
            # Decrement fish_plates_left, and update scoreboard.
            self.stats.fish_plates_left -= 1
            self.sb.prep_fish_plates()

            # Get rid of any remaining flying fish and kittens.
            self.fish_flys.empty()
            self.kittens.empty()

            # Create a new squad and center the ship.
            self._create_squad()
            self.fish_plate.center_fish_plate()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_kittens_bottom(self):
        """Check if any kitten has reached the bottom of the screen."""
        for kitten in self.kittens.sprites():
            if kitten.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the plate got hit.
                self._fish_plate_hit()
                break

    def _update_kittens(self):
        """Update the positions of all kittens in the squad."""
        self._check_squad_edges()
        self.kittens.update()

        # Look for kittens hitting the bottom of the screen.
        self._check_kittens_bottom()

        # Look for kitten-plate collisions.
        if pygame.sprite. spritecollideany(self.fish_plate, self.kittens):
            self._fish_plate_hit()

    def _create_squad(self):
        """Create the squad of kittens."""
        # Spacing between kittens is one kitten width and one kitten height.
        kitten = Kitten(self)
        kitten_width, kitten_height = kitten.rect.size

        current_x, current_y = kitten_width, kitten_height
        while current_y < (self.settings.screen_height - 3 * kitten_height):
            while current_x < (self.settings.screen_width - 2 * kitten_width):
                self._create_kitten(current_x, current_y)
                current_x += 2 * kitten_width
            
            # Finished a row; reset x value, and increment y value.
            current_x = kitten_width
            current_y += 2 * kitten_height

    def _create_kitten(self, x_position, y_position):
        """Create a kitten and place it in the row."""
        new_kitten = Kitten(self)
        new_kitten.x = x_position
        new_kitten.rect.x = x_position
        new_kitten.rect.y = y_position
        self.kittens.add(new_kitten)

    def _check_squad_edges(self):
        """Respond appropriately if any kitten has reached an edge."""
        for kitten in self.kittens.sprites():
            if kitten.check_edges():
                self._change_squad_direction()
                break
    
    def _change_squad_direction(self):
        """Drop the entire squad and change the squad's direction."""
        for kitten in self.kittens.sprites():
            kitten.rect.y += self.settings.squad_drop_speed
        self.settings.squad_direction *= -1

    def _update_screen(self):
        """Update imagees on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for fish in self.fish_flys.sprites():
            fish.blitme()
        self.fish_plate.blitme()
        self.kittens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ki = KittensInvasion()
    ki.run_game()
