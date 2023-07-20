import pygame
import random
from pygame.sprite import Sprite
from game.utils.constants import ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet


class Lurker(Sprite):
    ENEMY_WIDTH = 100
    ENEMY_HEIGHT = 120
    Y_POS = 0
    X_POS_RANGE = [300, 400, 500, 600, 700]
    SPEED_ON_Y = 5
    SPEED_ON_X = 3
    MOVES = { 0: 'left', 1: 'right'}
    INITIAL_SHOOTING_TIME = 1000
    FINAL_SHOOTING_TIME = 3000


    def __init__(self):
        self.image = ENEMY_2
        self.image = pygame.transform.scale(self.image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect(midtop = (random.choice(self.X_POS_RANGE), self.Y_POS))
        self.direction = self.MOVES[random.randint(0, 1)]
        self.movement_count = 0
        self.moves_before_change = random.randint(20, 50)
        self.type = 'enemy'
        current_time = pygame.time.get_ticks()
        self.shooting_time = random.randint(current_time + self.INITIAL_SHOOTING_TIME, current_time + self.INITIAL_SHOOTING_TIME)

    def update(self, enemies, game):
        self.rect.y += self.SPEED_ON_Y
        self.shoot(game.bullet_manager)

        if self.direction == self.MOVES[0]:
            self.rect.x -= self.SPEED_ON_X
        elif self.direction == self.MOVES[1]:
            self.rect.x += self.SPEED_ON_X

        self.handle_direction()

        if self.rect.top > SCREEN_HEIGHT:
            enemies.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_direction(self):
        self.movement_count += 1

        if (self.movement_count >= self.moves_before_change and self.direction == self.MOVES[1]) or self.rect.right >= SCREEN_WIDTH:
            self.direction = self.MOVES[0]
        elif self.movement_count >= self.moves_before_change and self.direction == self.MOVES[0] or self.rect.left <= 0:
            self.direction = self.MOVES[1]
        
        if (self.movement_count >= self.moves_before_change):
            self.movement_count = 0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()

        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(self.INITIAL_SHOOTING_TIME, self.FINAL_SHOOTING_TIME)