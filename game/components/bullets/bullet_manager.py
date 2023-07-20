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

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)

            if bullet.rect.colliderect(game.enemy) and bullet.owner == "player":
                game.enemy.remove(self)
        


    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.lurker_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 10:
            self.enemy_bullets.append(bullet)

        elif bullet.owner == "enemy" and len(self.lurker_bullets) < 10:
            self.enemy_bullets.append(bullet)

        elif bullet.owner == "player" and len(self.player_bullets) < 10:
            self.player_bullets.append(bullet)