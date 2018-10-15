from games.game import Game
from games.state import State

class StateManager:
    def __init__(self, game: Game, m, g):
        self.game = game
        self.m = m
        self.g = g
        self.root: State = game.gen_initial_state()

