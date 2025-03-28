import sys, pygame,random
from settings import Settings
from star import Star


class StarInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) # this variable contains the screen object, we also set the initial screen resolution
        self.settings.screen_width  = self.screen.get_rect().width  #assign settings class width to full screen's
        self.settings.screen_height = self.screen.get_rect().height #assign settings class height to full screen's
        self.bg_colors = self.settings.bg_color # setting a color object, later to be used as the background color of our game




        self.stars = pygame.sprite.Group()

        self.star = Star(self)
        pygame.display.set_caption("Star Invasion")
        
        self._create_galaxy()



    def _create_galaxy(self):
        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - star_width # x2 because between each alien and another, there is an equal space for an alien
        number_of_stars = available_space_x //(star_width*2)  #number of alien that can fit in screen 

        available_space_y = self.settings.screen_height -star_height #ships the screen can fit vertically
        number_rows = available_space_y //(2*star_height)



        for star_number in range(number_of_stars):
                for row_number in range(number_rows):
                    self._create_star(star_number,row_number)

    def _create_star(self,star_number,row_number):
        coordinates_variation_x = random.randint(-50,50)
        coordinates_variation_y = random.randint(-50,50)
        dead_or_alive_star = random.randint(1,3)
        if dead_or_alive_star != 1:
            

            star = Star(self)
            star_width,star_height = star.rect.size #width And height
            
            
            star.rect.x = (star_width + 2 * star_width * star_number)+coordinates_variation_x #coordinates of the queue ship


            star.rect.y = (star.rect.height +(2 *star.rect.height *row_number))+coordinates_variation_y
            self.stars.add(star)#add the created alien to sprite group       









    def run_game(self):
    #a function that contains main methods that the game runs on
    
        while True:
            self._check_events()
            self._update_screen()






    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT: # It is seemingle that we are gonna have multiple quitting event? and so we iterate checking all of them
                    sys.exit()






    def _update_screen(self):
            self.screen.fill(self.bg_colors) #this is the actual function that changes
            self.stars.draw(self.screen)
            pygame.display.flip() # this function updates the frame of the game window with made changes




if __name__ == "__main__":
    StarInvasion().run_game()
