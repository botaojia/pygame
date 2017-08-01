import pygame

class Game_sound():
	def __init__(self):
		self.player_fire = pygame.mixer.Sound('sound/player_fire.wav')
		self.enemy_s_down = pygame.mixer.Sound('sound/enemy_small_down.wav')
		self.player_down = pygame.mixer.Sound('sound/player_down.wav')
		self.enemy_b_hit = pygame.mixer.Sound('sound/enemy_big_hit.wav')

	def play_player_bullet_sound(self):
		self.player_fire.play()
	def play_enemy_s_down_sound(self):
		self.enemy_s_down.play()
	def play_enemy_b_hit_sound(self):
		self.enemy_b_hit.play()
	def play_player_down_sound(self):
		self.player_down.play()		