import pygame
from pygame.sprite import Sprite
from settings import Settings
class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        
        self.image = pygame.image.load(r"/home/yahya/Desktop/programming/some images/alien-ship1.png")
        self.rect = self.image.get_rect()

        #positioning of the ship
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) #storing the ship x position on a float for later uses