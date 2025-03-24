# the functionality of this calss is to store the settings of our alien invasion game


class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,0)
        self.ship_speed = 1

        #bullets related attributes
        self.bullet_speed = 1.0
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = (255,255,255)
        self.bulelts_limit = 5



