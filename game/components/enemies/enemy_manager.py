import pygame
from game.components.enemies.enemy import Enemy
from game.components.enemies.lurker import Lurker


class EnemyManager:
    def __init__(self):
        self.enemies = []

    def update(self):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies)
        
        self.add_lurker()

        for lurker in self.enemies:
            lurker.update(self.enemies)
        
        
    def draw(self, screen):
        for enemy in self. enemies:
            enemy.draw(screen)
        for lurker in self. enemies:
            lurker.draw(screen)

    def add_enemy(self):
        if len(self.enemies) < 7:
            enemy = Enemy()
            self.enemies.append(enemy)

    def add_lurker(self):
        if len(self.enemies) < 7:
            lurker = Lurker()
            self.enemies.append(lurker)