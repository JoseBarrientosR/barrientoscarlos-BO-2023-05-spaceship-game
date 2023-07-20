import pygame 

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []
        self.lurker_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player) and bullet.owner == 'enemy':
                game.playing = False
                pygame.time.delay(2000)
                break

        for bullet in self.lurker_bullets:
            bullet.update(self.lurker_bullets)

            if bullet.rect.colliderect(game.player) and bullet.owner == 'enemy':
                game.playing = False
                pygame.time.delay(2000)
                break

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.lurker_bullets:
            bullet.drwa(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 2:
            self.enemy_bullets.append(bullet)

        elif bullet.owner == "enemy" and len(self.lurker_bullets) < 2:
            self.enemy_bullets.append(bullet)