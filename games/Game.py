import abc


class Game:

    __metaclass__ = abc.ABCMeta

    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def gen_initial_states(self):
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.gen_initial_states.__name__)

    @abc.abstractmethod
    def gen_child_states(self, state):
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.gen_child_states.__name__)

    @abc.abstractmethod
    def is_winning(self, state):
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.is_winning.__name__)