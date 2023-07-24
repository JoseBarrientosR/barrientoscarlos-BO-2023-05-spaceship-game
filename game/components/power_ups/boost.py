from game.components.power_ups.power_up import PowerUp

from game.utils.constants import BOOST, BOOST_TYPE

class Boost(PowerUp):
    def __init__(self):
        super().__init__(BOOST, BOOST_TYPE)