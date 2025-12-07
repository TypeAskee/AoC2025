"""
Module to solve Day 7 for Advent of Code 2025.
Author: TypeAskee
"""


class TachyonMap:
    SPLITTER = "^"
    BEAM = "|"
    EMPTY = "."
    START = "S"

    def __init__(self, in_string: list[str]) -> None:
        self._map = []
        self._path_map = []
        if in_string[-1].strip() == "":
            in_string.pop(-1)
        self._build_map(in_string)
        self._build_path_map()

    def _build_map(self, in_string: list[str]) -> None:
        for line in in_string:
            self._map.append(line.strip())

    def _build_path_map(self) -> None:
        for line in self.map:
            tmp = [x for x in line.replace(".", "0")]
            tmp_2 = []
            for y in tmp:
                if y == "0":
                    tmp_2.append(int(y))
                elif y == "S":
                    tmp_2.append(1)
                else:
                    tmp_2.append(y)
            self._path_map.append(tmp_2)

    def calc_path(self) -> None:
        # Don't start on the highest row.
        for x in range(1, len(self.path_map)):
            for y in range(len(self.path_map[x])):
                if self.map[x - 1][y] == self.SPLITTER:
                    continue
                if self.map[x][y] == self.SPLITTER and self.map[x - 1][y] == self.BEAM:
                    self._path_map[x][y - 1] += self.path_map[x - 1][y]
                    self._path_map[x][y + 1] += self.path_map[x - 1][y]
                    continue
                if self.map[x][y] == self.BEAM:
                    self._path_map[x][y] += self.path_map[x - 1][y]

    def count_heat(self) -> int:
        return sum([x for x in self.path_map[-1] if isinstance(x, int)])

    def calc_next(self, idx: int) -> None:
        if idx != 0:
            locs = [i for i, val in enumerate(self.map[idx]) if val == self.BEAM]
        else:
            locs = [i for i, val in enumerate(self.map[idx]) if val == self.START]
        for loc in locs:
            if self.map[idx + 1][loc] == self.EMPTY:
                self._map[idx + 1] = (
                    self.map[idx + 1][:loc] + self.BEAM + self.map[idx + 1][loc + 1 :]
                )
            elif self.map[idx + 1][loc] == self.SPLITTER:
                self._map[idx + 1] = (
                    self.map[idx + 1][: loc - 1]
                    + self.BEAM
                    + self.SPLITTER
                    + self.BEAM
                    + self.map[idx + 1][loc + 2 :]
                )

    def beam_count(self, idx: int) -> int:
        beams = [i for i, val in enumerate(self.map[idx]) if val == self.BEAM]
        return len(beams)

    def split_count(self) -> int:
        total_count = 0
        for i, line in enumerate(self.map):
            # Skip the first line because we know there are no splitters there.
            if i == 0:
                continue
            locs = [j for j, val in enumerate(line) if val == self.SPLITTER]
            for loc in locs:
                if self.map[i - 1][loc] == self.BEAM:
                    total_count += 1
        return total_count

    @property
    def map(self) -> list[str]:
        return self._map

    @property
    def path_map(self) -> list[list[int]]:
        return self._path_map


def format_lines(in_string: list[str]) -> TachyonMap:
    return TachyonMap(in_string)


def calc_part_a(in_string: list[str]) -> int:
    """
    Calculate part A solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    map = format_lines(in_string)
    for x in range(len(map.map) - 1):
        map.calc_next(x)
    return map.split_count()


def calc_part_b(in_string: list[str]) -> int:
    """
    Calculate part B solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    map = format_lines(in_string)
    for x in range(len(map.map) - 1):
        map.calc_next(x)
    map.calc_path()
    return map.count_heat()


def main(in_string: list[str]) -> None:
    """
    Main function which calls the different parts
    and prints the answers!
    """
    ans_one = calc_part_a(in_string)
    print(f"The final answer for Part 1 is {ans_one}.")
    ans_two = calc_part_b(in_string)
    print(f"The final answer for Part 2 is {ans_two}.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="file path to input")

    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        all_input = f.readlines()

    main(all_input)
