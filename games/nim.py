from games.game import Game


class Nim(Game):

    def __init__(self, n=10, k=3):
        Game.__init__(self, "Nim")
        self.n = n  # Stone count
        self.k = k  # Max count of stones to remove

    def gen_initial_states(self):
        state = self.gen_state(None, None, 0, self.n)
        children = []
        for i in range(1, self.k+1):
            children.append(self.gen_state(state, 1, i, self.n))
        state["children"] = children
        return state

    def gen_child_states(self, state):
        player = 2 if state["player"] == 1 else 1
        states = []
        for i in range(1, min(state["n"], self.k) + 1):
            states.append(self.gen_state(state, player, i, state["n"]))
        return states

    def is_winning(self, state):
        return not state["n"]

    def gen_state(self, parent, player, k, n):
        return {"parent": parent, "player": player, "k": k, "n": n-k,
                "winning": not n-k, "children": [], "wins": 0, "visits": 0}

