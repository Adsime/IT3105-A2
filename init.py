from games.nim import Nim
from mcts.mcts import MCTS
from mcts.stateManager import StateManager, State
from players.human import Human
from players.ai import AI

nim = Nim([Human("Timmy"), Human("Bob")], "mix")
sman = StateManager(nim, 100, 100)
mcts = MCTS(sman)

state = sman.root
mcts.expand(state)
mcts.simulate(state)
best = mcts.get_best_child(state)
print(state.visits, state.wins)
print(best.n)
print([[s.q, s.visits, s.wins] for s in state.children])




#print(nim.gen_child_states(sta)