from games.game import Game
from games.state import State
import random


class NimState(State):

    def __init__(self, parent: State, player, n):
        self.super = State.__init__(self, parent, player)
        self.n = n

    def is_terminal(self):
        return self.n == 0

    def __copy__(self):
        copy = NimState(None, self.player, self.n)
        copy.children = self.children
        return copy

    def __add__(self, picked):
        return NimState(self, None, self.n - picked)

    def __eq__(self, other):
        return self.n == other.n

    def __hash__(self):
        return self.n


class Nim(Game):

    def __init__(self, players, p, n=10, k=3):
        Game.__init__(self, "Nim")
        self.players = players
        self.p = p
        self.n = n  # Stone count
        self.k = k  # Max count of stones to remove
        self.states = {}

    def gen_initial_state(self):
        self.states = {}
        state = NimState(None, None, self.n)
        self.states[hash(state)] = state
        self.current_player = random.choice(self.players) if self.p == "mix" else self.players[self.p]
        return state

    def gen_child_states(self, state: NimState):
        states = []
        p = self.current_player
        if state.player:
            p = self.players[(self.players.index(state.player) + 1) % len(self.players)]
        for i in range(1, min(state.n, self.k) + 1):
            s = state + i
            if not hash(s) in self.states:
                self.states[hash(s)] = s
            s.player, s.parent = p, state
            states.append(s)
        return states

    def new_game(self):
        state = self.gen_initial_state()
        print("\nNEW GAME")
        while not state.is_terminal():
            state.children = self.gen_child_states(state)
            state = self.current_player.request_input(self, state)
            print(self.current_player.name, "took", state.parent.n - state.n, "stones")
            self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]
        return state.player




