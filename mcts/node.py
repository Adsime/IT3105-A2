from games.state import State
from players.player import Player


class Node:

    def __init__(self, parent, state: State, player: Player):
        self.parent = parent
        self.state = state
        self.player = player
