from game.components.power_ups.power_up import PowerUp

from game.utils.constants import SPREENT, SHIELD_TYPE

class Spreent(PowerUp):
    def __init__(self):
        super().__init__(SPREENT, SHIELD_TYPE)