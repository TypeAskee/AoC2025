"""
Module to solve Day 5 for Advent of Code 2025.
Author: TypeAskee
"""


class Interval:
    def __init__(self, x: int, y: int):
        self.low = x
        self.high = y

    def __str__(self):
        return f"({self.low}, {self.high})"

    def __repr__(self):
        return f"({self.low}, {self.high})"


def union(first: Interval, second: Interval) -> Interval:
    if first.low <= second.low:
        x = first.low
    else:
        x = second.low
    if first.high >= second.high:
        y = first.high
    else:
        y = second.high
    return Interval(x, y)


def is_overlapping(first: Interval, second: Interval) -> bool:
    if first.low <= second.high and second.low <= first.high:
        return True
    return False


def remove_all_overlaps(in_values: list[Interval]) -> list[Interval]:
    overlaps_found = 1000
    while overlaps_found > 0:
        overlaps_found = 0
        for i in range(len(in_values)):
            test_intvl = in_values.pop(i)
            no_overlaps = True
            for idx, intvl in enumerate(in_values):
                if is_overlapping(intvl, test_intvl):
                    no_overlaps = False
                    overlaps_found += 1
                    tmp = union(intvl, test_intvl)
                    in_values.pop(idx)
                    in_values.append(tmp)
                    break
            if not no_overlaps:
                break
            in_values.append(test_intvl)

    return in_values


def calc_ranges(in_string: list[str]):
    all_valid_fresh = []
    all_things_to_check = []
    fresh_ranges = True
    for element in in_string:
        if element.strip() == "":
            fresh_ranges = False
            continue
        if fresh_ranges:
            tmp = element.strip().split("-")
            tmp = Interval(int(tmp[0]), int(tmp[1]))
            if len(all_valid_fresh) == 0:
                all_valid_fresh.append(tmp)
                continue
            did_not_overlap = True
            for idx, value in enumerate(all_valid_fresh):
                if is_overlapping(tmp, value):
                    all_valid_fresh.pop(idx)
                    all_valid_fresh.append(union(tmp, value))
                    did_not_overlap = False
                    break
            if did_not_overlap:
                all_valid_fresh.append(tmp)
        else:
            all_things_to_check.append(int(element))

    return all_valid_fresh, all_things_to_check


def calc_part_a(in_string: list[str]) -> int:
    """
    Calculate part A solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    all_valid, to_check = calc_ranges(in_string)
    num_fresh = 0
    for item in to_check:
        for range in all_valid:
            if range.low <= item <= range.high:
                num_fresh += 1
                break

    return num_fresh


def calc_part_b(in_string: list[str]) -> int:
    """
    Calculate part B solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    all_valid, _ = calc_ranges(in_string)
    all_valid = remove_all_overlaps(all_valid)
    num_values = 0
    for ele in all_valid:
        num_values += ele.high - ele.low + 1
    return num_values


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
