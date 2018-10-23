import random
from games.state import State
from games.game import Game
import numpy as np


class MCTS:

    def __init__(self, m):
        self.m = m

    def simulate(self, game: Game, state: State):
        for i in range(self.m):
            child = self.tree_search(game, state)
            self.expand(game, child)
            fin = self.do_random_walk(game, child)
            self.backprop(child, fin.player == child.player, 1)

    def do_random_walk(self, game: Game, state: State):
        if state.is_terminal():
            return state
        return self.do_random_walk(game, random.choice(game.gen_child_states(state, False)))

    def tree_search(self, game: Game, state: State):
        if not len(state.children):
            return state
        unvisited_states = [s for s in state.children if not s.visits]
        state = random.choice(unvisited_states) if len(unvisited_states) \
            else self.get_best_child(state, True)
        return self.tree_search(game, state)

    def get_best_child(self, state: State, explore=False):
        state_util = [s.get_uct(explore) for s in state.children]   # q +- u based on max for each child state
        idx = np.argmax(state_util) #if max else np.argmin(state_util)   # find node of least or most utility based on max
        return state.children[idx]

    def expand(self, game: Game, state: State):
        state.children = game.gen_child_states(state)

    def backprop(self, state: State, win, visits):
        state.update(1 if win else 0, visits)
        if state.parent:
            self.backprop(state.parent, not win, visits)
