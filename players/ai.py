from players.player import Player
from mcts.mcts import MCTS, StateManager


class AI(Player):
    def __init__(self, name):
        Player.__init__(self, name)


    def request_input(self):
        return