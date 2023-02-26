import numpy as np

DECK = range(1, 11)
ACTIONS = (HIT, STICK) = (0, 1)

DEALER_RANGE = range(1, 11)
PLAYER_RANGE = range(1, 22)
SHAPE = (len(DEALER_RANGE), len(PLAYER_RANGE), len(ACTIONS))

TERMINAL_STATE = 'TERMINAL'

COLOUR_PROBS = {'red': 1/3, 'black': 2/3}
COLOUR_COEFS = {'red': -1, 'black': 1}

def draw_card(colour=None):
    value = np.random.choice(DECK)
    if colour is None:
        colours, probs = zip(*COLOUR_PROBS.items())
        colour = np.random.choice(colours, p=probs)
    return {'value': value, 'colour':colour}

def bust(total):
    return (total < 1 or 21 < total)
