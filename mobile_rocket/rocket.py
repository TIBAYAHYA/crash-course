import pygame
from settings import Settings
class Rocket:
    def __init__(self,mr_game):
        self.screen = mr_game.screen
        self.settings = mr_game.settings
        self.screen_rect = self.screen.get_rect()
        self.rocket_image = pygame.image.load(r"C:\Users\maroc\OneDrive\Desktop\graphics\space_ship1.png")
        self.rocket_rect = self.rocket_image.get_rect()
        self.rocket_rect.center = self.screen_rect.center
        #checkers for game moving direction
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
         
        if self.moving_right and self.rocket_rect.right < self.screen_rect.right:
            self.rocket_rect.x += self.settings.rocket_speed  # 
        
        if self.moving_left and self.rocket_rect.left > self.screen_rect.left :
            self.rocket_rect.x -= self.settings.rocket_speed  
        if self.moving_up and self.rocket_rect.top > self.screen_rect.top:
            self.rocket_rect.y -=self.settings.rocket_speed
        if self.moving_down and self.rocket_rect.bottom < self.screen_rect.bottom:
            self.rocket_rect.y += self.settings.rocket_speed
        
        
    def blitme(self):
        self.screen.blit(self.rocket_image,self.rocket_rect) 