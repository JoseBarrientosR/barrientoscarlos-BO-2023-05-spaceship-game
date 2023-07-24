import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, BULLET_BOOST, SCREEN_HEIGHT



class Bullet(Sprite):
    PLAYER_IMAGE = pygame.transform.scale(BULLET, (10, 20))
    ENEMY_IMAGE = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    BOOST_IMAGE = pygame.transform.scale(BULLET_BOOST, (40, 60))
    BULLET_TYPES = { "player" : PLAYER_IMAGE, "enemy" : ENEMY_IMAGE}
    SPEED = 10


    def __init__(self, spaceship):
        self.image = self.BULLET_TYPES[spaceship.type]
        self.rect = self.image.get_rect(center = spaceship.rect.center)
        self.owner = spaceship.type

    def update(self, bullets):
        if self.owner == "player":
            self.rect.y -= 20

        if self.owner == "enemy":
            self.rect.y += 20


        if self.rect.top < 0 or self.rect.centery > SCREEN_HEIGHT:
            bullets.remove(self)

    

    def draw(self, screen):
        screen.blit(self.image, self.rect)

