# the functionality of this calss is to store the settings of our alien invasion game
#image files size recommanded is 100x100

class Settings:
    def __init__(self):
        #screen related settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (0,0,0)
        


        #ship related settings
        self.ship_image = r"/home/yahya/Desktop/programming/some images/space-ship.png" #player ship image file
        self.ship_speed = 5





        #bullets related settings
        self.bullet_speed = 2.0
        self.bullet_width = 10
        self.bullet_height = 10
        self.bullet_color = (255,255,255)
        self.bulelts_limit = 5

        #alien related settings
        self.alien_image1 = r"/home/yahya/Desktop/programming/some images/alien-ship1.png" 
        self.alien_image2 = r"/home/yahya/Desktop/programming/some images/alien-ship2.png"

        self.alien_speed = 1.0 #speed of which the aliens get relativly closer to the bottom of screen / playership

        self.fleet_drop_speed = 10

        self.fleet_direction = 1 # with positive representing right and negative being left directions




