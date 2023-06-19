import pygame
from game.components.enemies.enemy_7 import Enemy7
from game.utils.constants import HELLHAMMER

class Hellhammer(Enemy7):
    
    WIDTH = 400
    HEIGHT = 340
    
    def __init__(self):
        self.image = HELLHAMMER
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)