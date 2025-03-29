import pygame,sys
from settings import Settings
from keyTracker import KeyTracker
class KeyDisplayer:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) # this variable contains the screen object, we also set the initial screen resolution
        self.settings.width  = self.screen.get_rect().width  #assign settings class width to full screen's
        self.settings.height = self.screen.get_rect().height ##assign settings class height to full screen's
        pygame.display.set_caption("Keys Displayer")
        self.bg_color = self.settings.background_color
        self.key_tracker = KeyTracker(self)




    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()


    

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN: # conditioning for a key stroke event
                self.key_tracker.key_down = True
                self.key_pressed = event.key #we obtain the key object
                self.key_tracker.key_pressed = self.settings.key_name_map.get(self.key_pressed, f"Unknown key: {self.key_pressed}")
                
                #the attribute above is set to equal humanly readable key names
                

            elif event.type == pygame.KEYUP: #case of key up
                self.key_tracker.key_down = False









    def _update_screen(self):
        self.screen.fill(self.bg_color)

        self.key_tracker.update()
        self.key_tracker.blitme()


        pygame.display.flip()
        



if __name__ == "__main__":
    KeyDisplayer().run_game()