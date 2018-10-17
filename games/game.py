import abc
from games.state import State


class Game:

    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def gen_initial_state(self):
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.gen_initial_state.__name__)

    @abc.abstractmethod
    def gen_child_states(self, state: State):
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.gen_child_states.__name__)

    @abc.abstractmethod
    def is_winning(self, state: State):
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.is_winning.__name__)

    @abc.abstractmethod
    def new_game(self):
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.new_game.__name__)
