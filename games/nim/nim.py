from games.game import Game
from games.state import State
import random
from mcts.node import Node
import uuid

class NimState(State):

    def __init__(self, n, unique_states=False):
        self.super = State.__init__(self)
        self.n = n
        self.unique_states = unique_states
        self.id = uuid.uuid4()

    def is_terminal(self):
        return self.n == 0

    def option_text(self, parent):
        return str(parent.n - self.n)

    def __copy__(self):
        copy = NimState(self.n, self.unique_states)
        return copy

    def __add__(self, items):
        return NimState(self.n - items, self.unique_states)

    def __eq__(self, other):
        return self.n == other.n

    def __hash__(self):
        return hash(self.id if self.unique_states else self.n)


class Nim(Game):

    def __init__(self, players, first_player, n=10, k=3, verbose=False, memory_level=0, unique_states=False):
        Game.__init__(self, "Nim", players, first_player)
        self.n = n  # Stone count
        self.k = k  # Max count of stones to remove
        self.verbose = verbose
        self.memory_level=memory_level
        self.unique_states = unique_states

    def gen_initial_state(self):
        if self.memory_level < 2:
            self.states = {}
        state = NimState(self.n, self.unique_states)
        if not hash(state) in self.states:
            self.states[hash(state)] = state
        else:
            state = self.states[hash(state)]
        self.current_player = random.choice(self.players) if self.first_player == "mix" else self.players[self.first_player]
        return state

    def gen_child_states(self, state: State, save_new=False):
        if len(state.children):
            return state.children
        states = []
        for i in range(1, min(state.n, self.k) + 1):    # All possible moves from state
            s = state + i
            idx = hash(s)
            if not idx in self.states and save_new:
                self.states[idx] = s
            if idx in self.states:  #
                s = self.states[idx]
            states.append(s)
        return states

    def gen_child_nodes(self, node: Node):
        p = self.get_next_player(node.player)
        nodes = [Node(node, s, p) for s in self.gen_child_states(node.state)]
        return nodes

    def print_game_info(self, parent_state, current_state):
        if self.verbose:
            print("Player", self.current_player.name, "selects", parent_state.n - current_state.n,
                  "stones: Remaining stones =", current_state.n)

    def new_game(self):
        state = self.gen_initial_state()
        if self.verbose: print("\n------------- NEW GAME -------------")
        while not state.is_terminal():
            if self.memory_level < 1:
                self.states = {}
                state.reset()
            parent = state
            state = self.current_player.request_input(self, state)
            self.print_game_info(parent, state)
            if not state.is_terminal(): # Means the current player won
                self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]
        if self.verbose: print("Player", self.current_player.name, "wins")
        return self.current_player




