from games.nim import Nim
from mcts.mcts import MCTS
from mcts.stateManager import StateManager

nim = Nim()
sman = StateManager(nim)
mcts = MCTS(sman)
mcts.train(10)




#print(nim.gen_child_states(sta)