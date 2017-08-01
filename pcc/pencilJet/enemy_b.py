import random
import pygame
from pygame.sprite import Sprite
import random

class Enemy_b(Sprite):
    """A single big enemy class"""

    def __init__(self, ai_settings, screen):
        """Initialize the big enemy"""
        super(Enemy_b, self).__init__()
        self.screen = screen
        self.radius = 75
        self.shot_count = 0
 
        # Load the big enemy image, and set its rect attribute.
        self.image = pygame.image.load('images/enemy_b.png')
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()

        # Start big enemy at the top of screen randomly
        self.rect.x = random.randint(200, ai_settings.screen_width - 200)
        self.rect.y = -300

        # Store the enemy's exact position
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        
    def update(self, ai_settings):
        """Move the big enemy right or left."""
        self.y += (ai_settings.eb_speed_factor * ai_settings.time_passed_msec/3)
        self.rect.y = self.y

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
