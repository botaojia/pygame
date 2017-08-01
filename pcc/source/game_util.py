import sys
import pygame
from pygame.sprite import Group
from time import sleep
from bullet import Bullet
from enemy_s import Enemy_s
from enemy_b import Enemy_b
from ship_destroyed import Enemy_s_destroyed
from ship_destroyed import Enemy_b_destroyed
from ship_destroyed import Cursor_destroyed
from cursor import Cursor
from cloud import Cloud

def check_events(ai_settings, screen, cursor, stats, play_button):
    """Respond to mouse and key inputs"""
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
	        pygame.quit()
	        sys.exit()
       elif event.type == pygame.KEYDOWN:
	      	if event.key == pygame.K_ESCAPE:
	      		pygame.quit()
	      		sys.exit()

       mleft, mright, mmid = pygame.mouse.get_pressed()
       
       if stats.game_active == False and mleft == True:
           x, y = pygame.mouse.get_pos()
           button_clicked = play_button.rect.collidepoint(x, y)
           if button_clicked == True:
               stats.game_active = True
               cursor.reset(ai_settings, screen, stats)

       if stats.game_active == True:
           if mleft == True:
               cursor.is_firing = True
           else:
               cursor.is_firing = False

def player_fire_bullet(ai_settings, screen, cursor, player_bullets, gs):
    """player Fires a bullet"""
    if len(player_bullets) < ai_settings.player_bullets_allowed and \
       ai_settings.player_bullet_timer_msec >= ai_settings.player_bullet_freq:

        if ai_settings.since_enemy_big_down < 7500:
            player_bullets.add(Bullet(screen, cursor.rect.centerx-cursor.rect.width/3, cursor.rect.top, 0))
            player_bullets.add(Bullet(screen, cursor.rect.centerx+cursor.rect.width/3, cursor.rect.top, 0))
        else:
            player_bullets.add(Bullet(screen, cursor.rect.centerx-5, cursor.rect.top, 0))
        
        gs.play_player_bullet_sound()
        ai_settings.player_bullet_timer_msec = \
        ai_settings.player_bullet_timer_msec % ai_settings.player_bullet_freq

def init_cloud_once(ai_settings, screen, clouds):
    """initialize clouds when game begins, only called once"""
    for y in range(10, 800, 100):
        clouds.add(Cloud(ai_settings, screen, y))

def update_cloud(ai_settings, screen, clouds):
  # Get rid of small enemy that have disappeared.
    for c in clouds.copy():
        if c.rect.bottom >= ai_settings.screen_height + c.rect.height:
            clouds.remove(c)

    if len(clouds) < ai_settings.cloud_allowed and \
       ai_settings.cloud_timer_msec >= ai_settings.cloud_freq:

       c = Cloud(ai_settings, screen)
       clouds.add(c)
       ai_settings.cloud_timer_msec = 0

    clouds.update()

def update_player_bullets(ai_settings, screen, cursor, player_bullets, gs):
    # Get rid of bullets that have disappeared.
    if cursor.destroyed == True:
        return

    for b in player_bullets.copy():
        if b.rect.bottom <= 0:
            player_bullets.remove(b)

    if cursor.is_firing == True:
        player_fire_bullet(ai_settings, screen, cursor, player_bullets, gs)
    else:
        # Every left mouse button release will reset the timer.
        # As a result, clicking left moust button will shoot faster
        ai_settings.player_bullet_timer_msec = ai_settings.player_bullet_freq

    player_bullets.update(ai_settings)

def update_enemy_bullets(ai_settings, screen, ebs, enemy_bullets, gs):
    for b in enemy_bullets.copy():
        if b.rect.bottom >= ai_settings.screen_height or \
           b.rect.left >= ai_settings.screen_width or \
           b.rect.right <= 0:
            enemy_bullets.remove(b)

    if len(ebs) > 0 and \
       len(enemy_bullets) < ai_settings.enemy_bullets_allowed and \
       ai_settings.enemy_bullet_timer_msec >= ai_settings.enemy_bullet_freq:
        for eb in ebs.sprites():
            x = eb.rect.left + 59
            y = eb.rect.top + 129
            pi=3.1416
            angle = 3.5/4.0*pi
            enemy_bullets.add(Bullet(screen, x, y, angle))
            if ai_settings.difficulty_up_timer_msec > 30000:
                enemy_bullets.add(Bullet(screen, x, y, 2*pi - angle))
            if ai_settings.difficulty_up_timer_msec > 60000:
                enemy_bullets.add(Bullet(screen, x, y, pi))
            #gs.play_player_bullet_sound()
            ai_settings.enemy_bullet_timer_msec = \
            ai_settings.enemy_bullet_timer_msec % ai_settings.enemy_bullet_freq

    enemy_bullets.update(ai_settings)


def update_enemy_small(ai_settings, screen, ess, ebs):
	# Get rid of small enemy that have disappeared.
    for e in ess.copy():
        if e.rect.bottom >= ai_settings.screen_height + e.rect.height:
            ess.remove(e)

    for e in ebs.copy():
        if e.rect.bottom >= ai_settings.screen_height + e.rect.height:
            ebs.remove(e)

    if len(ebs) < ai_settings.enemy_big_allowed and \
       ai_settings.eb_timer_msec >= ai_settings.eb_freq:
       eb = Enemy_b(ai_settings, screen)
       ebs.add(eb)
       ai_settings.eb_timer_msec = 0

    if len(ess) < ai_settings.enemy_small_allowed and \
       ai_settings.es_timer_msec >= ai_settings.es_freq:
       if len(ebs) == 0:
           es = Enemy_s(ai_settings, screen)
       else:
           es = Enemy_s(ai_settings, screen, ebs.sprites()[0].rect.left, ebs.sprites()[0].rect.width)
       ess.add(es)
       ai_settings.es_timer_msec = 0

    ess.update(ai_settings)
    ebs.update(ai_settings)

def check_bullet_enemy_collisions(ai_settings, screen, ess, ebs, player_bullets, obj_destroyed, stats, gs):
    """Respond to bullet enemy_s enemy_b collisions."""
    # Remove any bullets and small enemy that have collided.
    collisions_es = pygame.sprite.groupcollide(ess, player_bullets, True, True, \
      pygame.sprite.collide_circle_ratio(0.9))

    for es in collisions_es:
      e = Enemy_s_destroyed(es.rect.centerx, es.rect.centery)
      obj_destroyed.add(e)
      stats.score += ai_settings.enemy_s_score
      stats.high_score = max(stats.high_score, stats.score)
      gs.play_enemy_down_sound()

    collisions_eb = pygame.sprite.groupcollide(ebs, player_bullets, False, True, \
      pygame.sprite.collide_circle_ratio(1.0))

    for eb in collisions_eb:
        eb.shot_count += 1
        gs.play_enemy_b_hit_sound()
        if eb.shot_count == ai_settings.eb_shot_need_to_destroy:
            ebd = Enemy_b_destroyed(eb.rect.centerx, eb.rect.centery)
            gs.play_enemy_down_sound()
            obj_destroyed.add(ebd)
            ebs.remove(eb)
            stats.score += ai_settings.enemy_b_score
            stats.high_score = max(stats.high_score, stats.score)
            ai_settings.since_enemy_big_down = 0

def check_bullet_cursor_collisions(ai_settings, screen, cursor, enemy_bullets, obj_destroyed, stats, gs):
    """Respond to bullet cursor collisions."""
    # Remove any bullets and small enemy that have collided.
    if cursor.do_not_check_collision(ai_settings) == True:
        return

    for b in enemy_bullets.copy():
      if pygame.sprite.collide_circle(cursor, b):
        c = Cursor_destroyed(b.rect.centerx, b.rect.centery)
        obj_destroyed.add(c)
        gs.play_player_down_sound()
        cursor.destroyed = True
        ai_settings.cursor_appear_delay = 0

def check_cursor_collisions(ai_settings, screen, cursor, ess, obj_destroyed, game_status, gs):
    """Respond to cursor enemy_s collisions."""
    if cursor.do_not_check_collision(ai_settings) == True:
        return

    for es in ess.copy():
      if pygame.sprite.collide_circle(cursor, es):
        e = Enemy_s_destroyed(es.rect.centerx, es.rect.centery)
        obj_destroyed.add(e)
        ess.remove(es)
        c = Cursor_destroyed(cursor.rect.centerx, cursor.rect.centery)
        obj_destroyed.add(c)
        gs.play_player_down_sound()        
        cursor.destroyed = True
        ai_settings.cursor_appear_delay = 0

def update_obj_destroyed(ai_settings, screen, obj_destroyed):   
    """draw destroyed ships"""
    if ai_settings.es_destroyed_timer_msec >= 40:
        for d in obj_destroyed.copy():
            if d.done == True:
                obj_destroyed.remove(d)
            else:
                d.update(ai_settings)
        ai_settings.es_destroyed_timer_msec = 0

def cursor_hit(ai_settings, screen, stats, cursor, ess, ebs, player_bullets, enemy_bullets, obj_destroyed):
    """cursor destroyed"""
    ai_settings.since_last_cursor_hit = 0
    if stats.cursor_left > 0 and ai_settings.cursor_appear_delay < 1000:
        return

    if stats.cursor_left > 0:
        if ai_settings.cursor_appear_delay < 1000:
            return
        else:
            cursor.reset(ai_settings, screen, stats)
    else:
        ebs.empty()
        ess.empty()
        player_bullets.empty()
        enemy_bullets.empty()
        stats.reset()

def redraw_objects(screen, cursor, player_bullets, enemy_bullets, ess, ebs):
      cursor.blitme(screen)
      for b in player_bullets.sprites():
        b.blitme()
      for b in enemy_bullets.sprites():
        b.blitme()
      for e in ess.sprites():
        e.blitme()
      for e in ebs.sprites():
        e.blitme()

def redraw_clouds(screen, clouds):
      for c in clouds.sprites():
        c.blitme()

def display_destroyed_objects(screen, obj_destroyed):
    obj_destroyed.draw(screen)
