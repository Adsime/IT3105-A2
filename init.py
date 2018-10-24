from games.nim.nim import Nim
from players.ai import AI
from players.human import Human

nim = Nim([AI("1", 100), AI("2", 100)], 0, 10, 3, verbose=True, memory_level=2, unique_states=False)
nim.run_batch(100)
