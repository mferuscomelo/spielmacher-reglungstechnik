from spielmacher.game import Game, GameConfig
from spielmacher.player import (
    Player,
    RandomPlayer,
    SimulatedPlayer,
)

MODEL_NAME = "TitForTatPlayer_base_svm"
NUM_ROUNDS = 10

MODEL_DIR = "models"
model_path = f"{MODEL_DIR}/{MODEL_NAME}.joblib"

p1 = SimulatedPlayer(model_path)
players: list[Player] = [
    RandomPlayer(),
    RandomPlayer(),
    RandomPlayer(),
    RandomPlayer(),
    RandomPlayer(),
    RandomPlayer(),
    RandomPlayer(),
    RandomPlayer(),
    RandomPlayer(),
    RandomPlayer(),
]

for p2 in players:
    config = GameConfig(p1, p2, NUM_ROUNDS, 0.0)
    game = Game(config)
    game.run()

    p1.print_moves()
    p2.print_moves()

    p1.reset()
    p2.reset()

    print("=========================================")
