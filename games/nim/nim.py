from games.game import Game
from games.state import State
import random


class NimState(State):

    def __init__(self, parent: State, player, players, n, grab_count):
        self.super = State.__init__(self, parent, player, players)
        self.n = n
        self.grab_count = grab_count

    def is_terminal(self):
        return not self.n

    def option_text(self):
        return self.grab_count


class Nim(Game):

    def __init__(self, players, p, n=10, k=3):
        Game.__init__(self, "Nim")
        self.players = players
        self.p = p
        self.n = n  # Stone count
        self.k = k  # Max count of stones to remove

    def gen_initial_state(self):
        fp = random.choice(self.players) if self.p == "mix" else self.players[self.p]
        state = NimState(None, fp, self.players, self.n, 0)
        return state

    def gen_child_states(self, state: NimState):
        states = []
        player = self.players[(self.players.index(state.player) + 1) % len(self.players)]
        for i in range(1, min(state.n, self.k) + 1):
            states.append(NimState(state, player, self.players, state.n - i, i))
        return states

    def is_winning(self, state: State):
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.is_winning.__name__)

    def new_game(self):
        state = self.gen_initial_state()
        root = state
        while not state.is_terminal():
            state = state.player.request_input(self, state)
            print("Player: '" + state.parent.player.name + "' chose action: " + str(state.grab_count))
            print("Remaining stones: " + str(state.n))
            print()
        print([c.q for c in root.children])





