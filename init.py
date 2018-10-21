from games.nim.nim import Nim
from players.ai import AI

nim = Nim([AI("Timmy", 100, 100), AI("Bob", 100, 100)], 0, 10, 3)

winners = {"Timmy": 0, "Bob": 0}

for i in range(100):
    winner = nim.new_game()
    winners[winner.name] += 1
    #print(str(i + 1) + "/1000")
print(winners.__str__())





#print(nim.gen_child_states(sta)