import sys,pygame
from settings import Settings
from ship import Ship

#a class to manage basic stuff like game launch
class AlienInvasion:

    # the initializing function of the game that auto runs
    def __init__(self):

        pygame.init() #initializing py game methods
        self.settings = Settings()  #object referance on an end to the settings class on settings.py
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height)) # this variable contains the screen object, we also set the initial screen resolution
        pygame.display.set_caption("Alien Invasion")
#(255,255,255) equals to the colors (reg,green,blue)
        self.bg_colors = (self.settings.bg_color) # setting a color object, later to be used as the background color of our game
        self.ship = Ship(self) # we set a Ship class variable, with It having acess
        # Ship(self) so the target class can access our function(as well as not crash out)
    def run_game(self):
        #a function that contains main methods that the game runs on
        
        while True:
            self._check_events()
            # a loop that constantly checks for user quitting input, I guess pygame doesnt have a built in one
            self._upldate_screen()

    
    
    
    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT: # It is seemingle that we are gonna have multiple quitting event? and so we iterate checking all of them
                    sys.exit()
                #key down case
                elif event.type == pygame.KEYDOWN: # conditioning for a key stroke event
                    if event.key == pygame.K_RIGHT: # conditioning for the key stroke being right arrow key
                        self.ship.moving_right =  True 
                    elif event.key == pygame.K_LEFT: # key stroke being left arrow
                        self.ship.moving_left = True

                #key up case
                elif event.type == pygame.KEYUP: #case of key up
                    if event.key == pygame.K_RIGHT: # the key up being right arrow
                          self.ship.moving_right = False
                    elif event.key == pygame.K_LEFT: # the key up being left arrow
                         self.ship.moving_left = False
    
    

    def _upldate_screen(self):
            self.screen.fill(self.bg_colors) #this is the actual function that changes
            self.ship.blitme() #run the bltime function from ship class, which just draws the ship image in ship rectangular
            self.ship.update()
            pygame.display.flip() # this function updates the frame of the game window with made changes
    
         
if __name__ == "__main__":
    AlienInvasion().run_game()
