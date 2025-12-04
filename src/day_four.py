"""
Module to solve Day 4 for Advent of Code 2025.
Author: TypeAskee
"""


class Map:
    EMPTY = "."
    ROLL = "@"

    def __init__(self, in_string: list[str]) -> None:
        self.in_string = in_string
        self._map = []
        self._build_map()

    def _build_map(self):
        for line in self.in_string:
            self._map.append(list(line.strip()))

    def calc_num_around(self, x: int, y: int) -> int:
        num_around = 0
        for x_check in [-1, 0, 1]:
            for y_check in [-1, 0, 1]:
                if not (x_check == 0 and y_check == 0):
                    if x + x_check < 0 or y + y_check < 0:
                        continue
                    try:
                        if self.map[x + x_check][y + y_check] == self.ROLL:
                            num_around += 1
                    except IndexError:
                        continue
        return num_around

    @property
    def map(self) -> list[list[str]]:
        return self._map

    def get_specific_element(self, x: int, y: int) -> str:
        return self.map[x][y]

    def remove_items(self, items_to_move: list[list[int]]) -> None:
        for item_loc in items_to_move:
            self._map[item_loc[0]][item_loc[1]] = self.EMPTY


def get_map(in_string: list[str]) -> Map:
    return Map(in_string)


def calc_part_a(in_string: list[str]) -> int:
    """
    Calculate part A solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    map = get_map(in_string)
    reachable_items = 0
    for x in range(len(map.map)):
        for y in range(len(map.map[x])):
            if map.get_specific_element(x, y) == "@":
                if map.calc_num_around(x, y) < 4:
                    reachable_items += 1
    return reachable_items


def calc_part_b(in_string: list[str]) -> int:
    """
    Calculate part B solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    map = get_map(in_string)
    items_removed = 0
    still_can_move = True
    while still_can_move:
        reachable_items = []
        for x in range(len(map.map)):
            for y in range(len(map.map[x])):
                if map.get_specific_element(x, y) == "@":
                    if map.calc_num_around(x, y) < 4:
                        reachable_items.append([x, y])
        if len(reachable_items) > 0:
            items_removed += len(reachable_items)
            map.remove_items(reachable_items)
        else:
            still_can_move = False
    return items_removed


def main(in_string: list[str]) -> None:
    """
    Main function which calls the different parts
    and prints the answers!
    """
    ans_one = calc_part_a(in_string)
    print(f"The final password for Part 1 is {ans_one}.")
    ans_two = calc_part_b(in_string)
    print(f"The final password for Part 2 is {ans_two}.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="file path to input")

    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        all_input = f.readlines()

    main(all_input)
