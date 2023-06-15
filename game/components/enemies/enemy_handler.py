from game.components.enemies.ship import Ship
from game.components.enemies.alien_ship import AlienShip
from game.components.enemies.alien_warship import AlienWarShip

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.enemies.append(Ship())
        self.enemies.append(AlienShip())
        self.enemies.append(AlienWarShip())
    
    def update(self):
        for enemy in self.enemies:
            enemy.update()
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)