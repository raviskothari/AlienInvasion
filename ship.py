import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        #Moving flag
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        #Draw the ship at it's current location
        self.screen.blit(self.image, self.rect)

    def update(self):
        #Update ship's position based on movement flag
        if self.moving_right == True:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.rect.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_left == True:
            if self.moving_left and self.rect.left > self.screen_rect.left:
                self.rect.centerx -= self.ai_settings.ship_speed_factor

    def center_ship(self):
        #Center the ship
        self.center = self.screen_rect.centerx