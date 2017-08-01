import random
import pygame
from pygame.sprite import Sprite
import random

class Enemy_s(Sprite):
    """A single small enemy class"""

    def __init__(self, ai_settings, screen, block_x = None, block_width = None):
        """Initialize the small enemy"""
        super(Enemy_s, self).__init__()
        self.screen = screen
        self.radius = 21
 
        # Load the enemy image, and set its rect attribute.
        self.image = pygame.image.load('images/enemy_s.png')
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()

        # Start small enemy at the top of screen randomly
        # block_x is the starting point of big enemy
        # block_width is the width of the big enemy

        if block_x == None:
             self.rect.x = random.randint(10, ai_settings.screen_width-10)
        else:
             x = random.randint(10, ai_settings.screen_width-10-block_width)
             if x <= block_x:
                 self.rect.right = x
             else:
                 self.rect.left = x + block_width


        self.rect.y = -50

        # Store the enemy's exact position.
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)
        
    def update(self, ai_settings):
        """Move the enemy location."""
        self.y += (ai_settings.es_speed_factor * ai_settings.time_passed_msec/3)
        self.rect.y = self.y

    def blitme(self):
        """Draw the enemy at its current location."""
        self.screen.blit(self.image, self.rect)
