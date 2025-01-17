import random
from enum import Enum
from abc import ABC, abstractmethod

type MoveHistory = list[list[Move]]
type ScoreHistory = list[list[Move]]


class Move(Enum):
    COOPERATE = "C"
    DEFECT = "D"


class Player(ABC):
    round_score: int
    total_score: int
    num_games: int
    move_history: MoveHistory
    score_history: ScoreHistory
    name: str = "GenericPlayer"

    @property
    def current_move_history(self) -> list[Move]:
        return self.move_history[self.num_games]
    
    @property
    def last_move(self) -> Move:
        return self.current_move_history[-1]

    def __init__(self):
        self.reset()

    def reset(self):
        self.round_score = 0
        self.total_score = 0
        self.num_games = 0
        self.move_history = [[]]
        self.score_history = [[]]

    def update_move_history(self, move: Move) -> None:
        self.move_history[self.num_games].append(move)

    def update_round_score(self, points: int) -> None:
        self.round_score += points
        self.score_history[self.num_games].append(self.round_score)

    def prepare_for_next_game(self) -> None:
        self.total_score += self.round_score
        self.round_score = 0
        self.num_games += 1
        self.score_history[self.num_games] = []
        self.move_history[self.num_games] = []

    def play(self, opponent_history: list[Move]) -> None:
        move = self._select_move(opponent_history)
        self.move_history.append(move)
        return move

    def print_moves(self) -> None:
        styled_history = [
            (
                f"\033[92m{move.value}\033[0m"
                if move == Move.COOPERATE
                else f"\033[91m{move.value}\033[0m"
            )
            for move in self.move_history[self.num_games]
        ]
        print(f"{self.name:<25} {' '.join(styled_history)}")

    @abstractmethod
    def _select_move(self, opponent_history: list[Move]) -> Move:
        pass


class CooperativePlayer(Player):
    """
    Always cooperates.
    """

    name: str = "CooperativePlayer"

        return Move.COOPERATE


class EgoisticPlayer(Player):
    """
    Always defects
    """

    name: str = "EgoisticPlayer"

        return Move.DEFECT


class RandomPlayer(Player):
    """
    Chooses moves randomly between cooperate and egoistic.
    """

    name: str = "RandomPlayer"

        return random.choice(list(Move))


class GrudgerPlayer(Player):
    """
    Cooperates until the opponent defects, then always defects.
    """

    name: str = "GrudgerPlayer"

        return Move.DEFECT if Move.DEFECT in opponent_history else Move.COOPERATE


class DetectivePlayer(Player):
    """
    Cooperates until the opponent defects twice in a row, then always defects.
    """

    name: str = "DetectivePlayer"
    defect: bool = False

    def _select_move(self, opponent_history: list[Move]) -> Move:
        move = Move.COOPERATE

        if self.defect:
            move = Move.DEFECT
        elif (
            len(opponent_history) >= 2
            and opponent_history[-1] == Move.DEFECT
            and opponent_history[-2] == Move.DEFECT
        ):
            self.defect = True
            move = Move.DEFECT

        return move


class TitForTatPlayer(Player):
    """
    Cooperates at first, then plays the opponent's last move.
    """

    name: str = "TitForTatPlayer"

        return Move.COOPERATE if not opponent_history else opponent_history[-1]


class ForgivingTitForTatPlayer(Player):
    """
    Cooperates until the opponent defects, then a 10% chance to forgive a defect
    """

    name: str = "ForgivingTitForTatPlayer"
    FORGIVE_PROBABILITY: int = 0.1  # 10% chance to forgive

    def _select_move(self, opponent_history: list[Move]) -> Move:
        if not opponent_history:
            return Move.COOPERATE
        elif (
            opponent_history[-1] == Move.DEFECT
            and random.random() < self.FORGIVE_PROBABILITY
        ):
            return Move.COOPERATE

        return opponent_history[-1]


class SimpletonPlayer(Player):
    """
    Cooperates on the first round. If opponent cooperates, the player repeats its last move. If the opponent defects, the player switches its last move.
    """

    name: str = "SimpletonPlayer"
    last_move: Move = Move.COOPERATE

    def _select_move(self, opponent_history: list[Move]) -> Move:
        move = Move.COOPERATE

        if not opponent_history:
            move = Move.COOPERATE
        elif opponent_history[-1] == Move.COOPERATE:
            move = self.last_move
        else:
            move = Move.DEFECT if self.last_move == Move.COOPERATE else Move.COOPERATE

        self.last_move = move
        return move
