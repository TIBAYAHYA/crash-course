# a class that takes care of the functionality of a ship
#the initial vriables are used to draw the image in screen,
#the rectaguled variables are used to locate and control the images more efficiently
import pygame
from settings import Settings
class Ship: 
    def __init__(self,ai_game): # the ai_game parameter is supposed to have a screen object
        # ai_game is just a way to access functions of the received class
        self.screen = ai_game.screen # storing screen object of the alien invasion game
        self.settings = ai_game.settings # settings class referenciation
        self.screen_rect = self.screen.get_rect() #we define the screen object above as rectangular
        
        
        
        self.image = pygame.image.load(r"/home/yahya/Desktop/programming/some images/space-ship.png") #storing the ship image
        self.rect = self.image.get_rect()# we object the ship image above as rectangle
        
        
        #
        self.rect.midbottom = self.screen_rect.midbottom #setting ship rectangular coordinates to midbottom
        #took so long to understand, but self.rect.midbottom is not a unique attribue, rather It represents
        # the button of the self.rect object, and It is bound to It
        
        
        self.moving_right = False # a function that checks If the ship is moving right
        self.moving_left =  False 
    def update(self):
            #If right key down and coordinates of ship didnt reach right screen edge
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed  # move ship by 1 pixel to the right
            #If left key down and coordinates of ship didnt reach left screen edge
        if self.moving_left and self.rect.left > self.screen_rect.left :
            self.rect.x -= self.settings.ship_speed  # move ship by 1 pixel to the left
        
    def blitme(self):
        self.screen.blit(self.image,self.rect) # drawing the ship image in the rectangular coordinates