"""
Module to solve Day 3 for Advent of Code 2025.
Author: TypeAskee
"""


def calc_part_a(in_string: list[str]) -> int:
    """
    Calculate part A solution!

    Loop through instructions and count the
    number of times that we end on a 0.

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    max_values = []
    for line in in_string:
        calc_line = [int(x) for x in line.strip()]
        max_value = max(calc_line[:-1])
        max_idx = calc_line.index(max_value)
        second_max_value = max(calc_line[max_idx + 1 :])
        max_values.append(max_value * 10 + second_max_value)
    return sum(max_values)


def calc_part_b(in_string: list[str]) -> int:
    """
    Calculate part B solution!

    Loop through instructions and count the number of
    times that we hit 0 as we went through.

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    max_values = []
    for line in in_string:
        calc_line = [int(x) for x in line.strip()]
        max_value = ""
        cur_idx = 0
        for i in range(12):
            if i == 0:
                tmp_max = max(calc_line[: -11 + i])
                cur_idx = calc_line.index(tmp_max)
            elif i == 11:
                tmp_max = max(calc_line[cur_idx + 1 :])
                cur_idx = calc_line[cur_idx + 1 :].index(tmp_max) + cur_idx + 1
            else:
                tmp_max = max(calc_line[cur_idx + 1 : -11 + i])
                cur_idx = calc_line[cur_idx + 1 :].index(tmp_max) + cur_idx + 1
            max_value += str(tmp_max)
        max_values.append(int(max_value))
    return sum(max_values)


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
