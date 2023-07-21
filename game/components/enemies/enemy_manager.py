import pygame
from game.components.enemies.enemy import Enemy
from game.components.enemies.lurker import Lurker


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
        
        

        for lurker in self.enemies:
            lurker.update(self.enemies, game)
        
        
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
        for lurker in self. enemies:
            lurker.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 2:
            enemy = Enemy()
            lurker = Lurker()
            self.enemies.append(lurker)
            self.enemies.append(enemy)


    def reset(self):
        self.enemies = []
    