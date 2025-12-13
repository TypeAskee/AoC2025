"""
Module to solve Day 9 for Advent of Code 2025.
Author: TypeAskee
"""

import numpy as np


def format_lines(in_string: list[str]):
    coords = []
    for line in in_string:
        tmp = line.strip().split(",")
        coords.append([int(tmp[0]), int(tmp[1])])
    return coords


def calc_part_a(in_string: list[str]) -> int:
    """
    Calculate part A solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    coords = format_lines(in_string)
    max_area = 0
    for coord in coords:
        for other_side in coords:
            if coord == other_side:
                continue
            area = (abs(coord[0] - other_side[0]) + 1) * (
                abs(coord[1] - other_side[1]) + 1
            )
            if area > max_area:
                max_area = area

    return max_area


def calc_part_b(in_string: list[str]) -> int:
    """
    Calculate part B solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    coords = format_lines(in_string)
    max_x = max([coord[0] for coord in coords])
    max_y = max([coord[1] for coord in coords])
    map = np.zeros((max_x + 2, max_y + 2), dtype=np.int16)
    return 0


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
