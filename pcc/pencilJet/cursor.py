import pygame
from pygame.sprite import Sprite

class Cursor(Sprite):

    def __init__(self, settings, screen, stats):
        """Initialize the cursor, and set its starting position."""
        super(Cursor, self).__init__()
        self.image = pygame.image.load('images/cursor.png').convert_alpha()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.radius = 30
        self.is_firing = False
        self.destroyed = False

    def reset(self, settings, screen, stats):
        stats.cursor_left -= 1
        self.settings = settings

        # Start cursor at the bottom center of the screen.
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom

        # Shoot flag
        self.is_firing = False
        self.destroyed = False
        
    def update(self):
        """Update the ship's position, based on cursor position."""
        if self.destroyed == False:
            x, y = pygame.mouse.get_pos()
            #calculating left-up corner position of cursor
            self.rect.x = x - self.image.get_width() / 2
            self.rect.y = y - self.image.get_height() / 2

    def do_not_check_collision(self, settings):
        if self.destroyed == True or settings.since_last_cursor_hit < 1000:
            return True
        else:
            return False

    def blitme(self, screen):
        """Draw the cursor at its current location."""
        if self.destroyed == False:
            screen.blit(self.image, self.rect)
