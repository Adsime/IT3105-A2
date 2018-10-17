import random
from games.state import State
from games.game import Game
import numpy as np


class MCTS:

    def __init__(self, m, g):
        self.m, self.g = m, g

    def simulate(self, game: Game, state: State):
        current_player = state.player
        for i in range(self.m):
            child = self.tree_search(state, current_player)
            wins = 0
            for j in range(self.g):
                wins += 1 if self.do_random_walk(game, child).parent.player == current_player else -1
            self.backpropagate(child, wins, self.g)

    def do_random_walk(self, game: Game, state: State):
        while not state.is_terminal():
            choices = game.gen_child_states(state)
            state = random.choice(choices)
        return state

    def tree_search(self, state: State, current_player):
        unvisited_states = [s for s in state.children if not s.visits]
        return random.choice(unvisited_states) if len(unvisited_states) > 0 \
            else self.get_best_child(state, current_player == state.player)

    def get_best_child(self, state: State, max=True):
        max = np.argmax([s.get_uct() for s in state.children]) if max \
            else np.argmin([s.q - s.u for s in state.children])
        return state.children[max]

    def expand(self, game: Game, state: State):
        state.children = game.gen_child_states(state)

    def backpropagate(self, state: State, wins, visits):
        state.update(wins, visits)
        if state.parent:
            self.backpropagate(state.parent, wins, visits)
