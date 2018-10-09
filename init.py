from games.Nim import Nim

nim = Nim()

win = False
states = nim.gen_initial_states()

while not win:
    layer = []
    for state in states:
        child_states = nim.gen_child_states(state)
        state["children"] = child_states
        for child_state in child_states:
            if child_state["winning"]:
                while child_state:
                    print(child_state["player"], child_state["n"], child_state["k"])
                    child_state = child_state["parent"]
                exit()
        layer += child_states
    states = layer

print(states)

#print(nim.gen_child_states(sta)