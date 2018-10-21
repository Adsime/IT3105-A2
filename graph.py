from games.state import State

def print_graph(state, tabs):
    print(tabs, state.n, "visits="+str(state.visits), "wins"+str(state.wins))
    tabs += "\t"
    for child in state.children:
        print_graph(child, tabs)
