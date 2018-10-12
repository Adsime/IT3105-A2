from games.game import Game


class StateManager:

    def __init__(self, game: Game):
        self.game = game
        self.root = game.gen_initial_states()

    def get_child_states(self, state):
        child_states = state["children"]
        if not len(child_states):
            child_states = self.game.gen_child_states(state)
        return child_states