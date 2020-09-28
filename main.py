import sys
import pygame


#####################################################
class Setting():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


#####################################################
class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)


#####################################################
class GameFunctions():

    def check_events(self, ship):
        """Respond to keypresses and mouse events."""
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.rect.centerx -= 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False

    def update_screen(self, ai_settings, screen, ship):
        """Update images on the screen and flip to the new screen."""

        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


#####################################################
def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    ai_settings = Setting()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen)
    gf = GameFunctions()

    while True:
        gf.check_events(ship)

        ship.update()

        gf.update_screen(ai_settings, screen, ship)


run_game()
