import numpy as np
from utils import draw_card, bust, DEALER_RANGE, PLAYER_RANGE, TERMINAL_STATE

class Enivronment:
    def __init__(self):
        self.reset()

    def reset(self, dealer=None, player=None):
        if dealer is None:
            dealer = draw_card()['value']
        self.dealer = dealer

        if player is None:
            player = draw_card()['value']
        self.player = player

    def observe(self):
        if not (self.dealer in DEALER_RANGE and self.player in PLAYER_RANGE):
            return TERMINAL_STATE
        
        return np.array((self.dealer, self.player))
    


