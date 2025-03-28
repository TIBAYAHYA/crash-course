import pygame
from pygame.sprite import Sprite
from settings import Settings   



class Star(Sprite):
    def __init__(self,SI_game):
        super().__init__()
        
        self.screen = SI_game.screen
        self.image = pygame.image.load(SI_game.settings.star_image) # loading the star image
        self.rect = self.image.get_rect() #rectangular of the star image


        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)




        