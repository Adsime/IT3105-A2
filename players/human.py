from players.player import Player


class Human(Player):

    def __init__(self, name):
        Player.__init__(self, name)

    def request_input(self):
        return input()