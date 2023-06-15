from game.components.enemies.ship import Ship
from game.components.enemies.alien_ship import AlienShip

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies.append(Ship())
        self.enemies.append(AlienShip())
    
    def update(self):
        for enemy in self.enemies:
            enemy.update()
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)