import joblib

from game import Game, GameConfig
from player import (
    Player,
    CooperativePlayer,
    EgoisticPlayer,
    RandomPlayer,
    GrudgerPlayer,
    DetectivePlayer,
    TitForTatPlayer,
    ForgivingTitForTatPlayer,
    SimpletonPlayer,
    EveryNthDefectorPlayer,
    SimulatedPlayer,
)

MODEL_NAME = "base_rfc"
NUM_ROUNDS = 10

MODEL_DIR = "models"
ENCODER_DIR = f"{MODEL_DIR}/encoder.joblib"
model_path = f"{MODEL_DIR}/{MODEL_NAME}.joblib"

p1 = SimulatedPlayer(model_path, ENCODER_DIR)
players: list[Player] = [
    CooperativePlayer(),
    EgoisticPlayer(),
    RandomPlayer(),
    GrudgerPlayer(),
    DetectivePlayer(),
    TitForTatPlayer(),
    ForgivingTitForTatPlayer(),
    SimpletonPlayer(),
    EveryNthDefectorPlayer(2),
    EveryNthDefectorPlayer(3),
    EveryNthDefectorPlayer(4),
    EveryNthDefectorPlayer(5),
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
