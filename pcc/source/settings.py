def update_timer(tick, timer):
    return (timer + tick) % 1000000

class Settings():
    """A class to store all static settings."""

    def __init__(self):
        """Initialize the game's static settings."""
        # screen settings
        self.screen_width = 800#480
        self.screen_height = 800#650
        self.bg_color = (255, 255, 255)
        self.play_button_centerx = self.screen_width/2
        self.play_button_centery = self.screen_height/8*7

        # cursor ship settings.
        self.cursor_limit = 3

        # all timers to control dynamic intervals
        self.player_bullet_timer_msec = 0 #since last player bullet was created
        self.es_timer_msec = 0  #since last small enemy was created
        self.enemy_bullet_timer_msec = 0 #since last enemy bullet was created
        self.es_destroyed_timer_msec = 0 #since last destroyed object was diplayed
        self.eb_timer_msec = 0 #small enemy appear interval
        self.enemy_big_allowed = 2
        self.eb_freq = 10000 #50

        # points of knocking down each enemy
        self.enemy_s_score = 10
        self.enemy_b_score = 200

        # could display setting
        self.cloud_speed_factor = 0.2
        self.cloud_timer_msec = 0
        self.cloud_allowed = 10
        self.cloud_freq = 4500

        self.player_bullets_allowed = 100
        
        self.difficulty_up_timer_msec = 0
        self.since_enemy_big_down = 10000
        self.since_last_cursor_hit = 1000
        self.cursor_appear_delay = 0
        self.update_dynamic_settings()

    def update_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.bullet_speed_factor = 0.5 + min(1.2, (int(self.difficulty_up_timer_msec) / int(20000)) * 0.1)

        # small enemy speed factor
        self.es_speed_factor = 0.5 + (int(self.difficulty_up_timer_msec) / int(10000)) * 0.1
        self.eb_speed_factor = 0.1 + (int(self.difficulty_up_timer_msec) / int(15000)) * 0.1
        self.enemy_small_allowed = 5 + min(20, int(self.difficulty_up_timer_msec) / int(10000))
        self.es_freq = 500 - min(425, int(self.difficulty_up_timer_msec) / int(5000) * 50)
        # enemy bullet create interval, every x msec
        self.enemy_bullet_freq = 3000 - min(2900, int(self.difficulty_up_timer_msec) / int(5000) * 100)
        self.enemy_bullets_allowed = 3 + min(12, int(self.difficulty_up_timer_msec) / int(30000) * 3)
        # x msec per bullet
        self.player_bullet_freq = 400 - min(320, int(self.difficulty_up_timer_msec) / int(20000) * 50)
        self.eb_shot_need_to_destroy = 5 + min(10, int(self.difficulty_up_timer_msec) / int(10000))

    def update_all_timers(self, tick):
        self.player_bullet_timer_msec = update_timer(tick, self.player_bullet_timer_msec)
        self.enemy_bullet_timer_msec = update_timer(tick, self.enemy_bullet_timer_msec)
        self.es_timer_msec = update_timer(tick, self.es_timer_msec)
        self.eb_timer_msec = update_timer(tick, self.eb_timer_msec)
        self.since_enemy_big_down = update_timer(tick, self.since_enemy_big_down)
        self.es_destroyed_timer_msec = update_timer(tick, self.es_destroyed_timer_msec)
        self.difficulty_up_timer_msec = update_timer(tick, self.difficulty_up_timer_msec)
        self.cloud_timer_msec = update_timer(tick, self.cloud_timer_msec)
        self.since_last_cursor_hit = update_timer(tick, self.since_last_cursor_hit)
        self.cursor_appear_delay = update_timer(tick, self.cursor_appear_delay)

    def rest_dynamic_settings(self):
        self.difficulty_up_timer_msec = 0
        self.since_enemy_big_down = 10000