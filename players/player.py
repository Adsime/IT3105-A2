import abc
from games.state import State
from mcts.mcts import MCTS, StateManager


class Player:

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def request_input(self, state):
        raise NotImplementedError(self.request_input.__name__)

    def reset(self):
        pass

    def __repr__(self):
        return self.name

