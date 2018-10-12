from mcts.stateManager import StateManager
import random


class MCTS:

    def __init__(self, state_manager: StateManager):
        self.state_manager = state_manager

    def search(self, state):
        if state["winning"]:
            return state
        return self.search(self.determine_next_state(state))

    def determine_next_state(self, state):
        children = self.state_manager.get_child_states(state)
        branch_values = []
        for child in children:
            if child["winning"]: return child
            branch_values.append(self.calculate_branch_value(child))
        return random.choice(children)

    def calculate_branch_value(self, state):
        pass

    def backpropagate(self, state):
        winner = state["player"]
        while state:
            state["visits"] += 1
            state["wins"] += 1 if state["player"] == winner else 0

    def train(self, episodes):
        for i in range(episodes):
            leaf_state = self.search(self.state_manager.root)
            self.backpropagate(leaf_state)




