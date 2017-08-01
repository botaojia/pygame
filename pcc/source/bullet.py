import pygame
import math
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, screen, x, y, shooting_angle):
        """Create a bullet object, at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.radius = 5
        self.image = pygame.image.load('images/bullet.png').convert_alpha()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()
        
        self.rect.centerx = x
        self.rect.centery = y
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        self.shooting_angle = shooting_angle

    def update(self, ai_settings):
        """Update the bullet's position."""
        self.y -= ai_settings.bullet_speed_factor * math.cos(self.shooting_angle) * ai_settings.time_passed_msec
        self.rect.y = self.y
        self.x -= ai_settings.bullet_speed_factor * math.sin(self.shooting_angle) * ai_settings.time_passed_msec
        self.rect.x = self.x

    def blitme(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
