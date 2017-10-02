import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        #Create a bullet object at ship's current position
        super().__init__()
        self.screen = screen

        #Create a bullet rect at (0,0) and then set the correct position
        #Since there is no bullet image, we create it from scratch using 'Rect' class and initialize it to (0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        #Next two lines positions the bullet in the correct location (the ships position). Since the bullet depends
        #on the ship, we use the 'Sprite' class
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #Move the bullet up the screen

        #Update decimal value of bullet
        self.y -= self.speed_factor

        #Update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        #Draw bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)

