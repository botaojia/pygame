import pygame
import random
from pygame.sprite import Sprite

class Cloud(Sprite):
    """A class to display cloud."""

    def __init__(self, ai_settings, screen, y=None):
        """Create cloud objects."""
        super(Cloud, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Create cloud rect at (0, 0), then set correct position.
        self.images = []
        self.images.append(pygame.image.load('images/cloud_1.png'))
        self.images.append(pygame.image.load('images/cloud_2.png'))
        self.images.append(pygame.image.load('images/cloud_3.png'))
        self.images.append(pygame.image.load('images/cloud_4.png'))
        self.images.append(pygame.image.load('images/cloud_5.png'))
        self.images.append(pygame.image.load('images/cloud_6.png'))

        load_which = random.randint(0,5)
        self.image = self.images[load_which]
        #self.image = pygame.transform.rotozoom(self.image, 0, 0.8)
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect()

        self.rect.centerx = random.randint(1,self.ai_settings.screen_width)
        if y == None:
            self.rect.y = random.randint(-80,2)
        else:
            self.rect.y = y

        # Store a decimal value for the cloud position.
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.cloud_speed_factor

    def update(self):
        """Move the cloud up the screen."""
        # Update the decimal position of the star.
        self.y += self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def blitme(self):
        """Draw the star to the screen."""
        self.screen.blit(self.image, self.rect)
