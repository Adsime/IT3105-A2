from games.game import Game
from games.state import State
import random


class NimState(State):

    def __init__(self, parent: State, player, players, n, k, grab_count):
        self.super = State.__init__(self, parent, player, players)
        self.n = n
        self.k = k
        self.grab_count = grab_count

    def is_terminal(self):
        return not self.n

    def option_text(self):
        return self.grab_count

    def get_next_states(self):
        states = []
        player = self.players[(self.players.index(self.player) + 1) % len(self.players)]
        for i in range(1, min(self.n, self.k) + 1):
            states.append(NimState(self, player, self.players, self.n - i, self.k, i))
        return states


class Nim(Game):

    def __init__(self, players, p, n=10, k=3):
        Game.__init__(self, "Nim")
        self.players = players
        self.p = p
        self.n = n  # Stone count
        self.k = k  # Max count of stones to remove

    def new_game(self):
        state = self.gen_initial_state()
        while not state.is_terminal():
            state = state.player.request_input(state)
            print("Player: '" + state.parent.player.name + "' chose action: " + str(state.grab_count))
            print("Remaining stones: " + str(state.n))

    def gen_initial_state(self):
        fp = random.choice(self.players) if self.p == "mix" else self.players[self.p]
        state = NimState(None, fp, self.players, self.n, self.k, 0)
        return state



