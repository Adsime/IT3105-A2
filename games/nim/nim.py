from games.game import Game
from games.state import State
import random
import time


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

    def __add__(self, vals):
        return NimState(self, vals[0], self.n - vals[1])


class Nim(Game):

    def __init__(self, players, p, n=10, k=3):
        Game.__init__(self, "Nim")
        self.players = players
        self.p = p
        self.n = n  # Stone count
        self.k = k  # Max count of stones to remove

    def gen_initial_state(self):
        self.current_player = random.choice(self.players) if self.p == "mix" else self.players[self.p]
        state = NimState(None, None, self.n)
        return state

    def gen_child_states(self, state: NimState):
        states = []
        p = self.current_player
        if state.player:
            p = self.players[(self.players.index(state.player) + 1) % len(self.players)]
        for i in range(1, min(state.n, self.k) + 1):
            states.append(state + (p, i))
        return states

    def new_game(self):
        state = self.gen_initial_state()
        print("\nNEW GAME")
        while not state.is_terminal():
            state.children = self.gen_child_states(state)
            state = self.current_player.request_input(self, state)
            print(self.current_player.name, "took", state.parent.n - state.n, "stones")
            self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]
            #print("Player: '" + state.parent.player.name + "' chose action: " + str(state.grab_count))
            #print("Remaining stones: " + str(state.n))
            #print()
        #time.sleep(2)
        return state.player




