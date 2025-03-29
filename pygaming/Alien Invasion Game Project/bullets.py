#this class represents the bullets our ship is gonna be firing
import pygame
from pygame.sprite import Sprite

class Bullets(Sprite):
    def __init__(self,ai_game):
        super().__init__()  #this is an inheritance from SPrite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

         #bullet rect
        self.bullet_rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        #placement of the bullet in the middle top of ship
        self.bullet_rect.midtop = ai_game.ship.rect.midtop
        # aligning bullet mid top with ship's midtop

        # storing the y of the bullet, later to be used so we can
        # make bullets move upwards
        
        self.y = float(self.bullet_rect.y)
        #why float?since rectangular object coordinates cannot be floats, this is in case the speed or starting position is a float, to align the average 
        #distance traveled with on screen with that on numbers,on 1.5 speed we get 1-3-4-6 instead of 1-2-3-4, which looks more real to the player

    def update(self):
        self.y -= self.settings.bullet_speed #bullet heading upwards
        self.bullet_rect.y = self.y #change bullet location
    

    def draw_bullet(self):

        pygame.draw.rect(self.screen,self.color,self.bullet_rect)