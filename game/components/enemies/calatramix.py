import pygame
from game.components.enemies.enemy_3 import Enemy3
from game.utils.constants import CALATRAMIX

class Calatramix(Enemy3):
    
    WIDTH = 60
    HEIGHT = 80
    
    def __init__(self):
        self.image = CALATRAMIX
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)