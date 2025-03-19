import pygame
from settings import Settings
class KeyDisplayer:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) # this variable contains the screen object, we also set the initial screen resolution
        self.settings.screen_width  = self.screen.get_rect().width  #assign settings class width to full screen's
        self.settings.screen_height = self.screen.get_rect().height ##assign settings class height to full screen's
        pygame.display.set_caption("Keys Displayer")
        self.bg_color = self.settings.background_color
