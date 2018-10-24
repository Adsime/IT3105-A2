from players.player import Player, Game, State


class Human(Player):

    def __init__(self, name):
        Player.__init__(self, name)

    def request_input(self, game: Game, state: State):
        options = game.gen_child_states(state, False)
        return options[self.query_user([s.option_text(state) for s in options])]

    def query_user(self, options):
        stringyfied_options = [str(o) for o in options]
        print("Please select one of the following options: " + options.__str__())
        inp = input()
        if inp == ('exit' or 'stop' or 'quit'):
            print("Exiting program as command '" + str(inp) + "' was entered.")
            exit()
        elif inp not in stringyfied_options:
            print(str(inp) + " is not a valid input.\n")
            return self.query_user(options)
        return stringyfied_options.index(inp)