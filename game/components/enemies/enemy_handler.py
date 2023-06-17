from game.components.enemies.ship import Ship
from game.components.enemies.calatramix import Calatramix
from game.components.enemies.covenant import Covenant
from game.components.enemies.icon_of_sin import IconOfSin

class EnemyHandler:
    def __init__(self):
        self.enemies = []
        self.number_enemy_destroyed = 0

    def update(self, bullet_handler, player):
        self.add_enemy()
        for enemy in self.enemies:
            self.colliderect_player(enemy, player)
            enemy.update(bullet_handler)
            if not enemy.is_alive :
                self.number_enemy_destroyed += 1
                self.remove_enemy(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def add_enemy(self):
        if len(self.enemies) < 3:
            self.enemies.append(Covenant())
            self.enemies.append(Ship())
            self.enemies.append(Calatramix())
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def colliderect_player(self,enemy, player):
        if(enemy.rect.colliderect(player.rect)):
            player.is_alive = False
    
    def reset(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
