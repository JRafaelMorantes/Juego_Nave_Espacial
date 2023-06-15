import pygame
from game.components.enemies.enemy_2 import Enemy2
from game.utils.constants import ENEMY_3

class AlienWarShip(Enemy2):
    
    WIDTH = 70
    HEIGHT = 80
    
    def __init__(self):
        self.image = ENEMY_3
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)