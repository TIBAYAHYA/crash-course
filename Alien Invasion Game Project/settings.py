# the functionality of this calss is to store the settings of our alien invasion game


class Settings:
    def __init__(self):
        #screen related attributes
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,0)
        
        #ship related attributes
        self.ship_image = r"/home/yahya/Desktop/programming/some images/space-ship.png"
        self.ship_speed = 5





        #bullets related attributes
        self.bullet_speed = 1.0
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = (255,255,255)
        self.bulelts_limit = 5

        #alien related attributes
        self.alien_image1 = r"/home/yahya/Desktop/programming/some images/alien-ship1.png"
        self.alien_image2 = r"/home/yahya/Desktop/programming/some images/alien-ship2.png"




