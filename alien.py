import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        #Initalize the alien and set its starting position
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #Start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        #Draw alien at current location
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        #Return true if alien is at edge of screen
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right) or self.rect.left <= 0:
            return True

    def update(self):
        #Move alien right
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
