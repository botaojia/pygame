import pygame

class Game_status():
    """Game status, score, statistics."""
    
    def __init__(self, ai_settings, screen):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.screen = screen
        self.high_score = 0
        self.life_image = pygame.image.load('images/life.png')
        self.life_image.set_colorkey(self.life_image.get_at((0,0)))
        self.life_rect = self.life_image.get_rect()
        self.life_rect.centerx = 45
        self.life_rect.centery = 40
        # score color
        self.text_color = (30,30,30)
        self.reset()

    def reset(self):
        # curosr number count
        self.cursor_left = self.ai_settings.cursor_limit

        # Start game in an inactive state.
        self.game_active = False

        # current game score
        self.score = 0

    def gen_score(self):
        """Convert score into a rendered image."""
        score_str = "{:,}".format(self.score)
        self.score_image = pygame.font.SysFont("comicsansms", 30).render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
        self.score_image.set_colorkey(self.score_image.get_at((0,0)))
            
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen.get_rect().right - 20
        self.score_rect.top = 20

    def gen_high_score(self):
        """Convert high score into a rendered image."""
        score_str = "HIGH:   " + "{:,}".format(self.high_score)
        self.high_score_image = pygame.font.SysFont("comicsansms", 30).render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
        self.high_score_image.set_colorkey(self.high_score_image.get_at((0,0)))
            
        # Display the score at the top right of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen.get_rect().right - 300
        self.high_score_rect.top = 20

    def gen_life(self):
        """Convert cursor left into a rendered image."""
        score_str = "{:,}".format(self.cursor_left)
        self.cursor_left_image = pygame.font.SysFont("comicsansms", 40).render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
        self.cursor_left_image.set_colorkey(self.cursor_left_image.get_at((0,0)))
            
        # Display the score at the top right of the screen.
        self.cursor_left_rect = self.cursor_left_image.get_rect()
        self.cursor_left_rect.right = self.screen.get_rect().right - 695
        self.cursor_left_rect.top = 11

    def display_score(self):
        self.gen_score()
        self.screen.blit(self.score_image, self.score_rect)

    def display_high_score(self):
        self.gen_high_score()
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def display_life(self):
        self.gen_life()
        self.screen.blit(self.life_image, self.life_rect)
        self.screen.blit(self.cursor_left_image, self.cursor_left_rect)

    def display_stats(self):
        self.display_score()
        self.display_high_score()
        self.display_life()
