# a class that takes care of the functionality of a ship
#the initial vriables are used to draw the image in screen,
#the rectaguled variables are used to locate and control the images more efficiently
import pygame
class Ship: 
    def __init__(self,ai_game): # the ai_game parameter is supposed to have a screen object
        # ai_game is just a way to access functions of the received class
        self.screen = ai_game.screen # storing screen object of the alien invasion game
        self.screen_rect = self.screen.get_rect() #we define the screen object above as rectangular
        
        self.image = pygame.image.load(r"C:\Users\maroc\OneDrive\Desktop\graphics\space_ship1.png") #storing the ship image
        self.rect = self.image.get_rect()# we object the ship image above as rectangle

        #
        self.rect.midbottom = self.screen_rect.midbottom #setting ship rectangular coordinates to midbottom

    def blitme(self):
        self.screen.blit(self.image,self.rect) # drawing the ship image in the rectangular coordinates