import pygame
from pygame.sprite import Sprite

class Ship_destroyed(Sprite):
    def __init__(self, x, y):
        super(Ship_destroyed, self).__init__()
        self.done = False
        self.index = 0

    def update(self, ai_settings):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''

        self.image = self.images[self.index]
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.index += 1

        if self.index == len(self.images):
        	self.done = True
        else:
        	self.done = False

class Enemy_s_destroyed(Ship_destroyed):
    def __init__(self, x, y):
        super(Enemy_s_destroyed, self).__init__(x, y)
        self.images = []
        self.images.append(pygame.image.load('images/ese1.png'))
        self.images.append(pygame.image.load('images/ese2.png'))
        self.images.append(pygame.image.load('images/ese3.png'))
        self.images.append(pygame.image.load('images/ese4.png'))
        self.images.append(pygame.image.load('images/ese5.png'))
        self.images.append(pygame.image.load('images/ese6.png'))
        self.image = self.images[self.index]
        self.rect = pygame.Rect(1, 1, 43, 45)
        self.rect.centerx = x
        self.rect.centery = y

class Enemy_b_destroyed(Ship_destroyed):
    def __init__(self, x, y):
        super(Enemy_b_destroyed, self).__init__(x, y)
        self.images = []
        self.images.append(pygame.image.load('images/ebe1.png'))
        self.images.append(pygame.image.load('images/ebe2.png'))
        self.images.append(pygame.image.load('images/ebe3.png'))
        self.images.append(pygame.image.load('images/ebe4.png'))
        self.images.append(pygame.image.load('images/ebe5.png'))
        self.images.append(pygame.image.load('images/ebe6.png'))
        self.images.append(pygame.image.load('images/ebe7.png'))
        self.images.append(pygame.image.load('images/ebe8.png'))
        self.images.append(pygame.image.load('images/ebe9.png'))
        self.images.append(pygame.image.load('images/ebe10.png'))
        self.images.append(pygame.image.load('images/ebe11.png'))
        self.images.append(pygame.image.load('images/ebe12.png'))
        self.image = self.images[self.index]
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = pygame.Rect(1, 1, 150, 190)
        self.rect.centerx = x
        self.rect.centery = y

class Cursor_destroyed(Ship_destroyed):
    def __init__(self, x, y):
        super(Cursor_destroyed, self).__init__(x, y)
        self.images = []
        self.images.append(pygame.image.load('images/player_e1.png'))
        self.images.append(pygame.image.load('images/player_e2.png'))
        self.images.append(pygame.image.load('images/player_e3.png'))
        self.images.append(pygame.image.load('images/player_e4.png'))
        self.images.append(pygame.image.load('images/player_e5.png'))
        self.images.append(pygame.image.load('images/player_e6.png'))
        self.images.append(pygame.image.load('images/player_e7.png'))
        self.images.append(pygame.image.load('images/player_e8.png'))
        self.images.append(pygame.image.load('images/player_e9.png'))
        self.image = self.images[self.index]
        self.rect = pygame.Rect(1, 1, 60, 74)
        self.rect.centerx = x
        self.rect.centery = y