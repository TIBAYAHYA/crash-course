#this is the remaking of the mid-creation alien invasion game, with some minor modification
# not much comments since we already have comments on the previous game
# comments on here and other files related to this game are pretty much for new stuff 
import pygame,sys
from settings import Settings
from rocket import Rocket
class MobileROcket:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        # settings creen to full screen mode, delete this part If you want the game to take settings class resolution
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width  = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        ##########################################
        pygame.display.set_caption("Mobile Ship")
        self.background_color = (self.settings.background_color)
        self.rocket = Rocket(self)
    def run_game(self):
        while True:
            self._check_events()
            self._upldate_screen()



    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys.exit()
                #key down case
                elif event.type == pygame.KEYDOWN: 
                    self._check_keydown_event(event)

                #key up case
                elif event.type == pygame.KEYUP: #case of key up
                    self._check_keyup_event(event)


    def _check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT: 
            self.rocket.moving_right =  True 
        elif event.key == pygame.K_LEFT: 
            self.rocket.moving_left = True
            #this is where we add the arrow key down and up events being pressed
        elif event.key == pygame.K_DOWN: 
            self.rocket.moving_down = True
        elif event.key == pygame.K_UP: 
            self.rocket.moving_up = True
            #game exits if q is pressed
        elif event.key == pygame.K_q:
             sys.exit()


    def _check_keyup_event(self,event):
        if event.key == pygame.K_RIGHT: 
                self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT: 
                self.rocket.moving_left = False 

        #this is where we add the conditionning for when the up and down arrow keys are no longer pressed
        elif event.key == pygame.K_DOWN: 
                self.rocket.moving_down = False 
        elif event.key == pygame.K_UP: 
                self.rocket.moving_up = False     
    
    def _upldate_screen(self):
            self.screen.fill(self.background_color) 
            self.rocket.blitme() 
            self.rocket.update()
            pygame.display.flip() 








if __name__ == "__main__":
    MobileROcket().run_game()