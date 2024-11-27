from player import (
    CooperativePlayer,
    EgoisticPlayer,
    DetectivePlayer,
    ForgivingTitForTatPlayer,
    TitForTatPlayer,
    RandomPlayer,
)
from tournament import Tournament

if __name__ == "__main__":
    players = [
        ForgivingTitForTatPlayer(),
        RandomPlayer(),
    ]
    tournament = Tournament(players, 10)
    tournament.run()
