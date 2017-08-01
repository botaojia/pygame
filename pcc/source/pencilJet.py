#!/usr/bin/python
import sys
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from game_sound import Game_sound
from settings import Settings
from cloud import Cloud
from cursor import Cursor
from bullet import Bullet
from enemy_s import Enemy_s
from play_button import Play_button
from game_status import Game_status
import game_util as gu


def run_pencilJet():
	pygame.init()
	clock = pygame.time.Clock()
	# reducing buffer size and attempting to fix sound lag
	pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=256)
	gs = Game_sound()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), 0, 32)
	pygame.display.set_caption("Pencil Jet Fight")

	play_button = Play_button(ai_settings, screen)
	stats = Game_status(ai_settings, screen)
	cursor = Cursor(ai_settings, screen, stats)
	player_bullets = Group()
	ess = Group() # small enemy
	ebs = Group() # big enemy
	obj_destroyed = Group()
	clouds = Group()
	enemy_bullets = Group()
	gu.init_cloud_once(ai_settings, screen, clouds)

	while True:
		gu.check_events(ai_settings, screen, cursor, stats, play_button)
		screen.fill(ai_settings.bg_color)
		stats.display_stats()
		#fix frame per second rate
		ai_settings.time_passed_msec = clock.tick(100)
		ai_settings.update_all_timers(ai_settings.time_passed_msec)
		ai_settings.update_dynamic_settings()
		gu.update_cloud(ai_settings, screen, clouds)

		if stats.game_active == False:
			play_button.blitme()
			ai_settings.rest_dynamic_settings()
		else:
			cursor.update()
			gu.update_player_bullets(ai_settings, screen, cursor, player_bullets, gs)
			gu.update_enemy_bullets(ai_settings, screen, ebs, enemy_bullets, gs)
			gu.update_enemy_small(ai_settings, screen, ess, ebs)
			gu.check_bullet_enemy_collisions(ai_settings, screen, ess, ebs, player_bullets, obj_destroyed, stats, gs)
			gu.check_bullet_cursor_collisions(ai_settings, screen, cursor, enemy_bullets, obj_destroyed, stats, gs)
			gu.check_cursor_collisions(ai_settings, screen, cursor, ess, obj_destroyed, stats, gs)

			if cursor.destroyed == True:
				gu.cursor_hit(ai_settings, screen, stats, cursor, ess, ebs, player_bullets, enemy_bullets, obj_destroyed)

			# re-draw all objects
			gu.redraw_objects(screen, cursor, player_bullets, enemy_bullets, ess, ebs)

		# Always update destroyed object, so the game animation looks normal when game ends
		gu.update_obj_destroyed(ai_settings, screen, obj_destroyed)
		gu.display_destroyed_objects(screen, obj_destroyed)
		gu.redraw_clouds(screen, clouds)
		pygame.display.flip()

run_pencilJet()
