import pygame
from game.components.enemies.enemy_5 import Enemy5
from game.utils.constants import DIABOLIC_SPACE_PRIEST

class DiabolicPriest(Enemy5):
    
    WIDTH = 150
    HEIGHT = 120
    
    def __init__(self):
        self.image = DIABOLIC_SPACE_PRIEST
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)