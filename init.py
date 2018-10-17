from games.nim.nim import Nim
from players.ai import AI

nim = Nim([AI("Timmy", 100, 100), AI("Bob", 100, 100)], "mix")
nim.new_game()





#print(nim.gen_child_states(sta)