import numpy as np

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
        # Root should not need updates
        if not self.parent:
            return
        self.q = self.wins/self.visits
        self.u = np.sqrt(np.log(self.parent.visits + visits)/self.visits)

    def get_uct(self):
        return self.q + self.u

    def get_random_child(self):
        raise NotImplementedError(self.get_random_child.__name__)
