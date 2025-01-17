import os
import csv
from player import Move, Player

MOVE_VALUES: dict = {Move.DEFECT: -1, Move.COOPERATE: 1}


class DataParser:
    __num_rounds: int
    __input_data: list[int]
    __columns: list[str]

    def __init__(self, num_rounds: int) -> None:
        self.__num_rounds = num_rounds
        self.__input_data = [0] * num_rounds * 2
        self.__columns = (
            [f"p1_{i+1}" for i in range(num_rounds)]
            + [f"p2_{i+1}" for i in range(num_rounds)]
            + ["move", "opponent"]
        )

    def save(self, p1: Player, p2: Player) -> None:
        p1_history = self.__transform_input(p1.current_move_history)
        p2_history = self.__transform_input(p2.current_move_history)

        # output_data = MOVE_VALUES.get(p1.last_move)
        output_data = p1.last_move.name
        data = self.__input_data + [output_data] + [p2.name]
        self.__write_to_file(p1.name, data)

        # Reset the input data
        self.__input_data = p1_history + p2_history

    def __transform_input(self, p1_history: list[Move]) -> list[int]:
        data = [MOVE_VALUES.get(move, 0) for move in p1_history]
        return data + [0] * (
            self.__num_rounds - len(data)
        )  # Pad the list to the required length

    def __write_to_file(self, filename: str, data: list):
        if not os.path.exists("data"):
            os.makedirs("data")

        with open(f"data/{filename}.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(self.__columns)
            writer.writerow(data)
