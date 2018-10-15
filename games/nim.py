from games.game import Game
from games.state import State
import random


class NimState(State):

    def __init__(self, parent: State, player, n):
        self.super = State.__init__(self, parent, player)
        self.n = n

    def is_terminal(self):
        return not self.n


class Nim(Game):

    def __init__(self, players, p, n=10, k=3):
        Game.__init__(self, "Nim")
        self.players = players
        self.p = p
        self.n = n  # Stone count
        self.k = k  # Max count of stones to remove

    def new_game(self):
        state = self.gen_initial_state()


    def gen_initial_state(self):
        fp = random.choice(self.players) if self.p == "mix" else self.players[self.p]
        state = NimState(None, fp, self.n)
        return state

    def gen_child_states(self, state: NimState):
        states = []
        player = self.players[(self.players.index(state.player) + 1) % len(self.players)]
        for i in range(1, min(state.n, self.k) + 1):
            states.append(NimState(state, player, state.n - i))
        return states

    @staticmethod
    def human_player():
        return input

