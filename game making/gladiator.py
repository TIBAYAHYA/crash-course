import pygame
class Gladiator:
    def __init__(self,bs_game):

        self.screen = bs_game.screen #game screen object
        self.screen_rect = self.screen.get_rect() # game screen rectangulation
 


        self.gladiator_image = pygame.image.load(r"C:\Users\maroc\OneDrive\Desktop\graphics\spartan_gladiator.png") #gladiator image store
        self.gladiator_rect = self.gladiator_image.get_rect() # get rect of the gladiator image
        self.gladiator_rect.center = self.screen_rect.center #reposition glad rect to center of window
    
    def blitme(self):
        self.screen.blit(self.gladiator_image,self.gladiator_rect) # drawing the gladiator image in rectangular location
