import pygame
from game.components.enemies.enemy_4 import Enemy4
from game.utils.constants import ICON_OF_SIN

class IconOfSin(Enemy4):
    
    WIDTH = 670
    HEIGHT = 430
    
    def __init__(self):
        self.image = ICON_OF_SIN
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)