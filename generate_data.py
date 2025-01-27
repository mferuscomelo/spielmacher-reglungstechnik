from data_parser import DataParser
from spielmacher.player import (
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
)
from spielmacher.game import Game, GameConfig

NUM_ROUNDS: int = 10

p1s: list[Player] = [
    CooperativePlayer(),
    EgoisticPlayer(),
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

p2s: list[Player] = [
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

for p1 in p1s:
    for p2 in p2s:
        parser = DataParser(NUM_ROUNDS)

        config = GameConfig(p1, p2, NUM_ROUNDS)
        game = Game(config)
        game.run(parser.save)

        p1.print_moves()
        p2.print_moves()

        p1.reset()
        p2.reset()

        print("=========================================")
