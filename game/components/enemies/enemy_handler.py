from game.components.enemies.ship import Ship
from game.components.enemies.calatramix import Calatramix
from game.components.enemies.covenant import Covenant
from game.components.enemies.icon_of_sin import IconOfSin
from game.components.enemies.diabolic_priest import DiabolicPriest
from game.components.enemies.slayer import Slayer
from game.components.enemies.hellhammer import Hellhammer
from game.components.enemies.recruiter_ship import RecruiterShip
from game.components.enemies.uldamar_ship import UldamarShip

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
        if len(self.enemies) < 1:
            if self.number_enemy_destroyed >= 100:
                self.enemies.append(IconOfSin())
                self.enemies.append(Covenant())
                self.enemies.append(Ship())
                self.enemies.append(Calatramix())
                self.enemies.append(DiabolicPriest())
                self.enemies.append(Slayer())
                self.enemies.append(RecruiterShip())
                self.enemies.append(UldamarShip())
            elif self.number_enemy_destroyed >= 75:
                self.enemies.append(IconOfSin())
            elif self.number_enemy_destroyed >= 54:
                self.enemies.append(Covenant())
                self.enemies.append(Ship())
                self.enemies.append(Calatramix())
                self.enemies.append(DiabolicPriest())
                self.enemies.append(Slayer())
                self.enemies.append(RecruiterShip())
                self.enemies.append(UldamarShip())
            elif self.number_enemy_destroyed >= 48:
                self.enemies.append(RecruiterShip())
                self.enemies.append(UldamarShip())
            elif self.number_enemy_destroyed >= 33:
                self.enemies.append(Covenant())
                self.enemies.append(Ship())
                self.enemies.append(Calatramix())
                self.enemies.append(DiabolicPriest())
                self.enemies.append(Slayer())
            elif self.number_enemy_destroyed >= 24:
                self.enemies.append(Hellhammer())
                self.enemies.append(DiabolicPriest())
                self.enemies.append(Slayer())
            else:
                self.enemies.append(Covenant())
                self.enemies.append(Ship())
                self.enemies.append(Calatramix())
                self.enemies.append(Ship())
                self.enemies.append(Covenant())
                self.enemies.append(Calatramix())
    
    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)
    
    def colliderect_player(self,enemy, player):
        if(enemy.rect.colliderect(player.rect)):
            player.is_alive = False
    
    def reset(self):
        self.enemies = []
        self.number_enemy_destroyed = 0
