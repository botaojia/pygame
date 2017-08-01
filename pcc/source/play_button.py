import pygame

class Play_button():

    def __init__(self, ai_settings, screen):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Set the dimensions and properties of the button.
        self.image = pygame.image.load("images/play_button.png").convert_alpha()
        self.image.set_colorkey(self.image.get_at((0,0)))

        # Build the button's rect object, and center it.
        self.rect = self.image.get_rect()
        self.rect.centerx = ai_settings.play_button_centerx
        self.rect.centery = ai_settings.play_button_centery

    def blitme(self):
        self.screen.blit(self.image, self.rect)
