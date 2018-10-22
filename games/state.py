import numpy as np
import abc


class State:

    def __init__(self, parent, player):
        self.parent: State = parent
        self.player = player
        self.children = []
        self.visits = 0
        self.wins = 0
        self.u = 0
        self.q = 0

    def is_terminal(self):
        raise NotImplementedError(self.is_terminal.__name__)

    def update(self, wins, visits):
        self.wins += wins
        self.visits += visits

    def get_uct(self, explore):
        q = self.wins / self.visits
        u = np.sqrt(np.log(self.parent.visits) / self.visits)
        return q + np.sqrt(2)*(u if explore else 0) #if max else 0#(self.u if max else -self.u)

    @abc.abstractmethod
    def option_text(self):
        raise NotImplementedError(self.option_text.__name__)

    @abc.abstractmethod
    def __copy__(self):
        raise NotImplementedError(self.__copy__.__name__)

    @abc.abstractmethod
    def __hash__(self):
        raise NotImplementedError(self.__hash__.__name__)

    def __eq__(self, other):
        raise NotImplementedError(self.__eq__.__name__)

