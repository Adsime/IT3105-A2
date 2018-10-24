from players.player import Player, Game, State
from mcts.mcts import MCTS


class AI(Player):
    def __init__(self, name, m):
        Player.__init__(self, name)
        self.brain = MCTS(m)

    def request_input(self, game: Game, state: State):
        self.brain.simulate(game, state)
        best_idx = self.brain.get_best_child(state)
        return game.gen_child_states(state)[best_idx]