import pygame
from game.components.enemies.enemy_8 import Enemy8
from game.utils.constants import RECRUITER

class RecruiterShip(Enemy8):
    
    WIDTH = 60
    HEIGHT = 80
    
    def __init__(self):
        self.image = RECRUITER
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        super().__init__(self.image)