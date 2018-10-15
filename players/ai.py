from players.player import Player, MCTS, StateManager

class AI(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.brain = MCTS()|


    def reset(self):
        pass


    def request_input(self, state):
        self.brain.expand(state)
        self.brain.simulate(state)
        return self.brain.get_best_child(state)