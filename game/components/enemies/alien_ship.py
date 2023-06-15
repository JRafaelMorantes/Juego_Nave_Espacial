import pygame
from game.components.enemies.enemy_3 import Enemy3
from game.utils.constants import ENEMY_2

class AlienShip(Enemy3):
    
    WIDTH = 60
    HEIGHT = 80
    
    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)