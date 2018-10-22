import abc
from games.state import State
from games.game import Game


class Player:

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def request_input(self, game: Game, state: State):
        raise NotImplementedError(self.request_input.__name__)

