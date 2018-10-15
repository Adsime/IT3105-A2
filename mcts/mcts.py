from mcts.stateManager import StateManager
import random
from games.state import State
import numpy as np

class MCTS:

    def __init__(self, state_manager: StateManager):
        self.state_manager = state_manager

    def simulate(self, state: State):
        current_player = state.player
        for i in range(self.state_manager.m):
            child = self.tree_search(state, current_player)
            wins = 0
            for j in range(self.state_manager.g):
                wins += 1 if self.do_random_walk(child).player != current_player else 0
            self.backpropagate(child, wins, self.state_manager.g)

    def do_random_walk(self, state: State):
        while not state.is_terminal():
            choices = self.state_manager.get_child_states(state)
            state = random.choice(choices)
        return state

    def tree_search(self, state: State, current_player):
        unvisited_states = [s for s in state.children if not s.visits]
        return random.choice(unvisited_states) if len(unvisited_states) > 0 \
            else self.get_best_child(state, current_player != state.player)


    def get_best_child(self, state: State, max=True):
        max = np.argmax([s.get_uct() for s in state.children]) if max \
            else np.argmin([s.q - s.u for s in state.children])
        return state.children[max]

    def expand(self, state: State):
        state.children = self.state_manager.get_child_states(state)

    def backpropagate(self, state: State, wins, visits):
        state.update(wins, visits)
        if state.parent:
            self.backpropagate(state.parent, wins, visits)

