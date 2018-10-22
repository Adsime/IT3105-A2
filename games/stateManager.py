from games.game import Game
from games.state import State

class StateManager:
    def __init__(self, game: Game):
        self.game = game
        self.states = {}
