from games.state import State


class Node:

    def __init__(self, parent, state: State, player):
        self.parent = parent
        self.state = state
        self.player = player

    def __copy__(self):
        return Node(self.parent, self.state.__copy__(), self.player)
