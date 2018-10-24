import random
from games.state import State
from games.game import Game
import numpy as np
from mcts.node import Node


class MCTS:

    def __init__(self, m):
        self.m = m

    def simulate(self, game: Game, state: State):
        """
        Used to run all the tree calls in one step
        :param game: Game
        :param state: State
        """
        root_node = Node(None, state, game.current_player)
        for i in range(self.m):
            child = self.tree_search(game, root_node)
            self.expand(game, child.state)
            fin = self.do_random_walk(game, child)
            self.backprop(child, fin.player, 1)

    def tree_search(self, game: Game, node: Node):
        """
        Finds the the next leaf node based on a tree policy
        :param game: Game
        :param node: Node
        :return: Node
        """
        if not len(node.state.children):    # Means we hit a leaf node
            return node
        children = game.gen_child_nodes(node)
        node = children[self.get_best_child(node.state, True)]
        return self.tree_search(game, node)

    def do_random_walk(self, game: Game, node: Node):
        """
        Does a random walk from a given node until a leaf node is hit
        :param game: Game
        :param node: Node
        :return: Node
        """
        if node.state.is_terminal():    # Means we hit a lead node
            return node
        node = random.choice(game.gen_child_nodes(node))
        return self.do_random_walk(game, node)

    def get_best_child(self, state: State, explore=False):
        """
        Return the index of the child with best utility score (experience + exploration factor)
        :param state: State
        :param explore: bool
        :return: int
        """
        state_util = [s.get_uct(state, explore) for s in state.children]   # q +- u based on max for each child state
        return np.argmax(state_util)

    def expand(self, game: Game, state: State):
        """
        Expands a state, assigning child states. These children may have other parents, but children are reused.
        :param game: Game
        :param state: State
        """
        state.children = game.gen_child_states(state, True)

    def backprop(self, node: Node, winner, visits):
        """
        Updates every state in the parent chain from the given node
        :param node: Node
        :param winner: Player
        :param visits: int - not strictly needed here, but might come in useful for doing multiple simulations from a
                             leaf node
        """
        node.state.update(1 if winner == node.player else 0, visits)
        if node.parent:
            self.backprop(node.parent, winner, visits)
