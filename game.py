from player import Player, Move

SCORE_MAP = {
    (Move.COOPERATE, Move.COOPERATE): (3, 3),
    (Move.DEFECT, Move.DEFECT): (1, 1),
    (Move.DEFECT, Move.COOPERATE): (5, 0),
    (Move.COOPERATE, Move.DEFECT): (0, 5),
}


class Game:
    __p1: Player
    __p2: Player
    __rounds: int

    def __init__(self, player1: Player, player2: Player, rounds: int) -> None:
        self.__p1 = player1
        self.__p2 = player2
        self.__rounds = rounds

    def run(self) -> Player:
        for _ in range(self.__rounds):
            self.__play_round()

        return self.__p1 if self.__p1.score > self.__p2.score else self.__p2

    def get_scores(self) -> tuple[int, int]:
        return self.__p1.score, self.__p2.score

    def __play_round(self) -> None:
        # Get moves from players, letting them know the history of the other player
        move1 = self.__p1.play(self.__p2.history)
        move2 = self.__p2.play(self.__p1.history)

        self.__update_scores(move1, move2)

    def __update_scores(self, move1: Move, move2: Move) -> None:
        scores = SCORE_MAP[(move1, move2)]
        self.__p1.update_score(scores[0])
        self.__p2.update_score(scores[1])
