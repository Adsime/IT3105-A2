import abc


class Player:

    def __init__(self, name):
        self.name = name

    @abc.abstractclassmethod
    def request_input(self):
        raise NotImplementedError(self.request_input.__name__)

    def reset(self):
        pass

    def __repr__(self):
        return self.name

