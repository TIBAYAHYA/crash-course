
import pygame
class KeyTracker:
    def __init__(self,KD):
        self.screen = KD.screen # keyDisplay class acess
        self.settings = KD.settings #settings class access
        
        self.screen_rect = self.screen.get_rect() # big screen rectangular acess
        self.key_tracker_rect = self.screen
        self.key_pressed = ""
        self.key_down = False





#since update is called before blitme on our main loop, we can afford to not define self.text_surface and self.text_rect at our previous function




    def update(self):
        self.text_surface = self.settings.font.render(self.key_pressed, True, (255, 255, 255)) #this is the text surface
        self.text_rect = self.text_surface.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2)) #this is the text rectangle




    def blitme(self):
        self.screen.blit(self.text_surface, self.text_rect)

