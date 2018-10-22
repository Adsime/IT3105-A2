from players.player import Player, Game, State
from mcts.mcts import MCTS
import graph


class AI(Player):
    def __init__(self, name, m, g):
        Player.__init__(self, name)
        self.brain = MCTS(m)

    def request_input(self, game: Game, state: State):
        sim_state = state#.__copy__()
        self.brain.simulate(game, sim_state)
        best = self.brain.get_best_child(sim_state)
        children = sim_state.children
        #graph.print_graph(sim_state, "")
        return state.children[children.index(best)]