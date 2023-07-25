import pygame
import random
from game.components.power_ups.boost import Boost
from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD
from game.components.power_ups.spreent import Spreent

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(5000, 10000)
        self.duration = random.randint(3000, 5000)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.has_power_up = True
                game.player.power_up_type = power_up.type
                if power_up.type == "Speedboost":
                    game.game_speed = self.rect.y + 5
                game.player.power_up_time_up = power_up.start_time + self.duration
                if isinstance(power_up, Shield):
                    game.player.set_image(SPACESHIP_SHIELD, (65, 75))
                elif isinstance(power_up, Boost):
                    game.player.set_image(SPACESHIP_SHIELD, (65, 75))
                elif isinstance(power_up, Spreent):
                    game.player.set_image(SPACESHIP_SHIELD, (65, 75))
                self.power_ups.remove(power_up)




    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
        for power_up in self.power_ups:
            power_up.draw(screen)

    def generate_power_up(self):
        power_up = Shield()
        self.when_appears += random.randint(5000, 10000)
        self.power_ups.append(power_up)
        power_up = Boost()
        self.when_appears += random.randint(10000, 15000)
        self.power_ups.append(power_up)
        power_up = Spreent()
        self.when_appears += random.randint(10000, 15000)
        self.power_ups.append(power_up)


    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(now + 5000, now + 10000)