from mcts.node import Node
from games.state import State


class Game:

    def __init__(self, name, players, first_player):
        self.players = players
        self.first_player = first_player
        self.name = name
        self.current_player = None
        self.states = {}
        self.score = {}
        self.reset_score()

    def reset_score(self):
        """
        Resets the internal score tracking
        """
        for player in self.players:
            self.score[player.name] = 0

    def run_batch(self, batch_size=1):
        """
        Runs 'batch_size' amount of games and tracks the win score.
        :param batch_size:
        :return:
        """
        self.reset_score()
        for i in range(batch_size):
            winner = self.new_game()
            self.score[winner.name] += 1
        print("\n------------- Batch results (" + str(batch_size) + " batches) -------------")
        for player in self.players:
            name = player.name
            score = self.score[name]
            print("Player", name, "wins", score, "of", batch_size, "(" + str(round(100*score/batch_size, 2)) + "%).")

    def get_next_player(self, player):
        p = self.current_player
        if player:
            next_idx = (self.players.index(player) + 1) % len(self.players)
            p = self.players[next_idx]
        return p

    def gen_initial_state(self):
        """
        Generates the initial state of the game
        :return: State
        """
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.gen_initial_state.__name__)

    def gen_child_states(self, state: State, save_new=False):
        """
        Generates all possible child states based on a state and returns them
        :param state:
        :param save_new: bool - used during expansion to track all generated states
        :return: list of State
        """
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.gen_child_states.__name__)

    def gen_child_nodes(self, node: Node):
        """
        Wraps all possible child states in a node object and returns them
        :param node: Node
        :return: list of Node
        """
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.gen_child_nodes.__name__)

    def new_game(self):
        """
        Starts a new game and returns the winning player
        :return: Player
        """
        raise NotImplementedError("Game " + self.name + " is missing implementation for "
                                  + self.new_game.__name__)
