import pygame
from game.components.enemies.enemy_6 import Enemy6
from game.utils.constants import SLAYER

class Slayer(Enemy6):
    
    WIDTH = 190
    HEIGHT = 130
    
    def __init__(self):
        self.image = SLAYER
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)