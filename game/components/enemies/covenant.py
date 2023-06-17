import pygame
from game.components.enemies.enemy_2 import Enemy2
from game.utils.constants import COVENANT

class Covenant(Enemy2):
    
    WIDTH = 150
    HEIGHT = 120
    
    def __init__(self):
        self.image = COVENANT
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)