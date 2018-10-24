import numpy as np


class State:

    def __init__(self):
        self.children = []
        self.visits = 0
        self.wins = 0

    def update(self, wins, visits):
        """
        Updated used in back-propagation
        :param wins: int
        :param visits: int
        """
        self.wins += wins
        self.visits += visits

    def get_uct(self, parent, explore):
        """
        Evaluates the value of the state based on experience
        :param explore: flag to factor exploration as well as experience
        :return: float
        """
        q = self.wins / (self.visits + 1)
        u = np.sqrt(np.log(parent.visits) / (self.visits + 1))
        return q + (np.sqrt(2)*(u if explore else 0))

    def reset(self):
        self.children = []
        self.visits = 0
        self.wins = 0

    def option_text(self, parent):
        """
        Returns the option which represents this state
        :return: str
        """
        raise NotImplementedError(self.option_text.__name__)

    def is_terminal(self):
        """
        Determines if the state is terminal or not
        :return: bool
        """
        raise NotImplementedError(self.is_terminal.__name__)

    def __copy__(self):
        """
        Creates a new instance of State with the same internal values
        :return: State
        """
        raise NotImplementedError(self.__copy__.__name__)

    def __add__(self, items):
        """
        Creates a new state (following self), using 'items'
        :param items: options used to create next state
        :return: State
        """
        raise NotImplementedError(self.__add__.__name__)

    def __hash__(self):
        """
        Used to identify a state
        :return: int
        """
        raise NotImplementedError(self.__hash__.__name__)

    def __eq__(self, other):
        """
        Compares two states
        :param other: State
        :return: bool
        """
        raise NotImplementedError(self.__eq__.__name__)

