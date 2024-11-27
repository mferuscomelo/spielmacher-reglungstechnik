import matplotlib.pyplot as plt
from matplotlib.widgets import Button

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

    def plot_scores(self) -> None:
        fig, ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)
        self.__current_round = 0

        def plot_round(round_index):
            p1_scores = self.__p1.score_history
            p2_scores = self.__p2.score_history

            ax.clear()
            ax.set_ylim(0, max(p1_scores + p2_scores) + 5)

            p1_score = p1_scores[round_index]
            p2_score = p2_scores[round_index]

            rects = ax.bar(
                [self.__p1.__class__.__name__, self.__p2.__class__.__name__],
                [p1_score, p2_score],
            )
            ax.bar_label(rects, padding=3)
            ax.set_title(f"Scores after round {round_index}")
            plt.draw()

        def next(event):
            if self.__current_round < self.__rounds:
                self.__current_round += 1
                plot_round(self.__current_round)

        def prev(event):
            if self.__current_round > 0:
                self.__current_round -= 1
                plot_round(self.__current_round)

        axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
        axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
        bnext = Button(axnext, "Next")
        bnext.on_clicked(next)
        bprev = Button(axprev, "Previous")
        bprev.on_clicked(prev)

        plot_round(self.__current_round)
        plt.show()

    def __play_round(self) -> None:
        # Get moves from players, letting them know the history of the other player
        move1 = self.__p1.play(self.__p2.move_history)
        move2 = self.__p2.play(self.__p1.move_history)

        self.__update_scores(move1, move2)

    def __update_scores(self, move1: Move, move2: Move) -> None:
        scores = SCORE_MAP[(move1, move2)]
        self.__p1.update_score(scores[0])
        self.__p2.update_score(scores[1])
