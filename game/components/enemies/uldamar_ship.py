import pygame
from game.components.enemies.enemy_9 import Enemy9
from game.utils.constants import ULDAMAR

class UldamarShip(Enemy9):
    
    WIDTH = 60
    HEIGHT = 80
    
    def __init__(self):
        self.image = ULDAMAR
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)