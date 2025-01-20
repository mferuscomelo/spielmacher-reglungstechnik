from spielmacher.tournament import Tournament
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

players = [
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


def callback(p1: Player, p2: Player):
    print(f"{p1.name} vs {p2.name}: {p1.round_score} - {p2.round_score}")
    p1.print_moves()
    p2.print_moves()


if __name__ == "__main__":
    tournament = Tournament(players, 10)
    tournament.run(callback)
