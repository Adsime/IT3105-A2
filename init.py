from games.nim import Nim
from mcts.mcts import MCTS
from mcts.stateManager import StateManager, State
from players.human import Human
from players.ai import AI

nim = Nim([AI("Timmy"), AI("Bob")], "mix")
sman = StateManager(nim, 100, 100)

nim.new_game()





#print(nim.gen_child_states(sta)