import numpy as np
from utils import draw_card, bust
from utils import DEALER_RANGE, PLAYER_RANGE, TERMINAL_STATE, COLOUR_PROBS, COLOUR_COEFS


class Enivronment:
    def __init__(self, dealer=None, player=None):
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

    def step(self, action):
        if action == 'HIT':
            card = draw_card()
            self.player += COLOUR_COEFS[card['colour']]*card['value']

            if bust(self.player):
                next_state, reward = TERMINAL_STATE, -1

            else:
                next_state, reward = (self.dealer, self.player), 0

        elif action == 'STICK':
            while 0 < self.dealer < 17:
                card = draw_card()
                self.dealer += COLOUR_COEFS[card['colour']]*card['value']

            next_state = TERMINAL_STATE
            
            if bust(self.dealer):
                reward = 1
            else:
                reward = int(self.player > self.dealer) - \
                    int(self.player < self.dealer)

        else:
            raise ValueError("something went wrong")
