import random
from enum import Enum
from abc import ABC, abstractmethod


class Move(Enum):
    COOPERATE = "C"
    DEFECT = "D"


class Player(ABC):
    score: int
    history: list[Move]

    def __init__(self):
        self.score: int = 0
        self.history: list[Move] = []

    def play(self, opponent_history: list[Move]) -> None:
        move = self._play_move(opponent_history)
        self.history.append(move)
        return move

    def update_score(self, score: int) -> None:
        self.score += score

    def print_moves(self) -> None:
        styled_history = [
            (
                f"\033[92m{move.value}\033[0m"
                if move == Move.COOPERATE
                else f"\033[91m{move.value}\033[0m"
            )
            for move in self.history
        ]
        print(f"{self.__class__.__name__:<25} {' '.join(styled_history)}")

    @abstractmethod
    def _play_move(self, opponent_history: list[Move]) -> Move:
        pass


class CooperativePlayer(Player):
    """
    Always cooperates.
    """

    def _play_move(self, opponent_history: list[Move]) -> Move:
        return Move.COOPERATE


class EgoisticPlayer(Player):
    """ """

    def _play_move(self, opponent_history: list[Move]) -> Move:
        return Move.DEFECT


class RandomPlayer(Player):
    """
    Chooses moves randomly between cooperate and egoistic.
    """

    def _play_move(self, opponent_history: list[Move]) -> Move:
        return random.choice(list(Move))


class GrudgerPlayer(Player):
    """
    Cooperates until the opponent defects, then always defects.
    """

    def _play_move(self, opponent_history: list[Move]) -> Move:
        if Move.DEFECT in opponent_history:
            return Move.DEFECT
        return Move.COOPERATE


class PavlovPlayer(Player):
    """
    Cooperates on the first round, then repeats the opponent's last move.
    """

    def _play_move(self, opponent_history: list[Move]) -> Move:
        if not opponent_history:
            return Move.COOPERATE
        return opponent_history[-1]


class DetectivePlayer(Player):
    """
    Cooperates until the opponent defects twice in a row, then always defects.
    """

    def _play_move(self, opponent_history: list[Move]) -> Move:
        if (
            len(opponent_history) >= 2
            and opponent_history[-1] == Move.DEFECT
            and opponent_history[-2] == Move.DEFECT
        ):
            return Move.DEFECT
        return Move.COOPERATE


class TitForTatPlayer(Player):
    """
    Cooperates at first, then plays the opponent's last move.
    """

    def _play_move(self, opponent_history: list[Move]) -> Move:
        if not opponent_history:
            return Move.COOPERATE

        return opponent_history[-1]


class ForgivingTitForTatPlayer(Player):
    """
    Cooperates until the opponent defects, then a 10% chance to forgive a defect
    """

    def _play_move(self, opponent_history: list[Move]) -> Move:
        if not opponent_history:
            return Move.COOPERATE
        if (
            opponent_history[-1] == Move.DEFECT
            and random.random() < 0.1  # 10% chance to forgive
        ):
            return Move.COOPERATE

        return opponent_history[-1]
