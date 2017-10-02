import sys, pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    #Initialize game and create the screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Draw the ship
    ship = Ship(ai_settings, screen)

    #Make a group to store the bullets in
    bullets = Group()

    #Start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets  )
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()


