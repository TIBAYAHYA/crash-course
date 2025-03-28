import sys,pygame
from settings import Settings
from ship import Ship
from bullets import Bullets
from alien import Alien
#a class to manage basic stuff like game launch
class AlienInvasion:

    # the initializing function of the game that auto runs
    def __init__(self):

        pygame.init() #initializing py game methods
        self.settings = Settings()  #object referance on an end to the settings class on settings.py
                                            #this means take coordinates from left top to down right
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) # this variable contains the screen object, we also set the initial screen resolution
        self.settings.screen_width  = self.screen.get_rect().width  #assign settings class width to full screen's
        self.settings.screen_height = self.screen.get_rect().height #assign settings class height to full screen's
        self.alien_speed = self.settings.alien_speed

        self.bullets = pygame.sprite.Group() #group of bullets to get updated
        self.aliens  = pygame.sprite.Group()
        self.ship = Ship(self)
        self._create_fleet()

        pygame.display.set_caption("Alien Invasion")
#(255,255,255) equals to the colors (reg,green,blue)
        self.bg_colors = self.settings.bg_color # setting a color object, later to be used as the background color of our game
         # we set a Ship class variable, with It having acess
        # Ship(self) so the target class can access our function(as well as not crash out)
    
        #this function basically creates an alien and adds It to the sprite group
    def _create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size #width And height
        available_space_x = self.settings.screen_width - (alien_width*2) # x2 because between each alien and another, there is an equal space for an alien
        number_of_aliens = available_space_x //(alien_width*2)  #number of alien that can fit in screen 
        
        
        
        ship_height = self.ship.rect.height #height of the ship

        available_space_y = self.settings.screen_height -(3*alien_height)-ship_height #ships the screen can fit vertically
        number_rows = available_space_y //(2*alien_height)

        for alien_number in range(number_of_aliens): #iterate over number of aliens
            for row_number in range(number_rows):
                self._create_alien(alien_number=alien_number,row_number=row_number)


    def _create_alien(self,alien_number,row_number):
            alien = Alien(self)
            alien_width,alien_height = alien.rect.size #width And height
            
            alien.x = alien_width + 2 * alien_width * alien_number #coordinates of the queue ship
            alien.rect.x = alien.x # assiging of the calculations to the coordinates

            alien.rect.y = alien.rect.height +(2 *alien.rect.height *row_number)
            self.aliens.add(alien)#add the created alien to sprite group       






 
    
    
    
    
    
    
    def run_game(self):
        #a function that contains main methods that the game runs on
        
        while True:
            self._check_events()
            # a loop that constantly checks for user quitting input, I guess pygame doesnt have a built in one
            

            self._update_bullets() # this function updates the bullets
            
            #getting rid of bullets outside the screen
            
            self._update_aliens()

            self._upldate_screen()


            
    
    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT: # It is seemingle that we are gonna have multiple quitting event? and so we iterate checking all of them
                    sys.exit()
                #key down case
                elif event.type == pygame.KEYDOWN: # conditioning for a key stroke event
                    self._check_keydown_event(event)

                #key up case
                elif event.type == pygame.KEYUP: #case of key up
                    self._check_keyup_event(event)
                





    def _check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT: # conditioning for the key stroke being right arrow key
            self.ship.moving_right =  True 
        elif event.key == pygame.K_LEFT: # key stroke being left arrow
            self.ship.moving_left = True
            #game exits if q is pressed
        elif event.key == pygame.K_q:
             sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet() # send the bullets










    def _check_keyup_event(self,event):
        if event.key == pygame.K_RIGHT: # the key up being right arrow
                self.ship.moving_right = False
        elif event.key == pygame.K_LEFT: # the key up being left arrow
                self.ship.moving_left = False 
    










    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bulelts_limit: #if the number of bullets is less than the limit of bullets
            new_bullet = Bullets(self) 
            self.bullets.add(new_bullet) #add bullet to








    def _update_bullets(self):
            self.bullets.update()  # this updates every single bullet in the group bullets     
            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.bullet_rect.bottom <= 0:
                    self.bullets.remove(bullet) 




    def _update_aliens(self):
        self.aliens.update()





    def _upldate_screen(self):
            self.screen.fill(self.bg_colors) #this is the actual function that changes
            self.ship.blitme() #run the bltime function from ship class, which just draws the ship image in ship rectangular
            self.ship.update()
            
            for bullet in self.bullets.sprites(): #iterate  over every bullet in the sprite group
                bullet.draw_bullet() #call the drawing function in bullets class
            self.aliens.draw(self.screen)
            pygame.display.flip() # this function updates the frame of the game window with made changes
         
if __name__ == "__main__":
    AlienInvasion().run_game()
