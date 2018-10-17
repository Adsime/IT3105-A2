from players.player import Player, Game, State
from mcts.mcts import MCTS


class AI(Player):
    def __init__(self, name, m, g):
        Player.__init__(self, name)
        self.brain = MCTS(m, g)

    def reset(self):
        pass

    def request_input(self, game: Game, state: State):
        self.brain.expand(game, state)
        self.brain.simulate(game, state)
        return self.brain.get_best_child(state)