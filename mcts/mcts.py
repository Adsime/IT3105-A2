import random
from games.state import State
from games.game import Game
import numpy as np


class MCTS:

    def __init__(self, m):
        self.m = m

    def simulate(self, game: Game, state: State):
        child = state
        for i in range(self.m):
            self.expand(game, child)
            child = fin = self.tree_search(state, game.current_player)
            if not child.is_terminal():
                fin = self.do_random_walk(game, child)
            self.backpropagate(child, 1 if fin.player == game.current_player else -1, 1)

    def do_random_walk(self, game: Game, state: State):
        if state.is_terminal():
            return state
        return self.do_random_walk(game, random.choice(game.gen_child_states(state)))

    def tree_search(self, state: State, current_player):
        if not len(state.children):
            return state
        unvisited_states = [s for s in state.children if not s.visits]
        state = random.choice(unvisited_states) if len(unvisited_states) \
            else self.get_best_child(state, current_player == state.player)
        return self.tree_search(state, current_player)

    def get_best_child(self, state: State, max=True):
        state_util = [s.get_uct(max) for s in state.children]   # q +- u based on max for each child state
        idx = np.argmax(state_util) if max else np.argmin(state_util)   # find node of least or most utility based on max
        return state.children[idx]

    def expand(self, game: Game, state: State):
        state.children = game.gen_child_states(state)

    def backpropagate(self, state: State, wins, visits):
        state.update(wins, visits)
        if state.parent:
            self.backpropagate(state.parent, wins, visits)
