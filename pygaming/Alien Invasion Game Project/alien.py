import pygame
from pygame.sprite import Sprite
from settings import Settings
class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings  = ai_game.settings
        
        self.image = pygame.image.load(r"/home/yahya/Desktop/programming/some images/alien-ship1.png")
        self.rect = self.image.get_rect()

        #positioning of the alien ship at x being with and y being height? to make sure an alien ship fits in all edges, but we dont actually place one there
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x) #storing previous position of the ship

        # update the aliens location? move them to the right uh oh!!!
    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        
        self.rect.x = self.x

    #function checks If aliens reach edges of the screen
    def check_edges(self):
        screen_rect = self.screen.get_rect()  #get the screen rectangular


        if self.rect.right >= screen_rect.right or self.rect.left <=screen_rect.left:
            return True