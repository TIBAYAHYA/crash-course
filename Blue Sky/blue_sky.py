import pygame,sys

from settings import Settings
from gladiator import Gladiator

class BlueSky:
    def __init__(self):
        pygame.init()
        self.settings = Settings() #initialize the game settings from Settings class
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Blue Sky") # the name of the game window
        self.bg_colors = self.settings.bg_color #settings color
        self.gladiator = Gladiator(self)
    def run_game(self):
        while True:
                
            self._check_events()
            self._update_screen()




    def _check_events(self):
        #this checks for quit event
        for event in pygame.event.get():
            if event ==quit:
                sys.exit()

    def _update_screen(self):
        #a split function updates screen color and draws gladiatorin his corresponding rectangular as well as display everything
        self.screen.fill(self.bg_colors)
        self.gladiator.blitme()
        pygame.display.flip()

    
if __name__ == "__main__":
    BlueSky().run_game()