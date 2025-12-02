"""
Module to solve Day 1 for Advent of Code 2025.
Author: TypeAskee
"""


def create_data(in_string: str | list[str]) -> list[str]:
    """
    Creates a prepared list of strings containing the commands.
    This list should only contain elements that are ready to be
    cast as strings.

    Parameters:
        in_string (str | list[str]) The input file

    Returns:
        list[str] The organized list of instructions in string form.
    """
    if isinstance(in_string, str):
        out = in_string.replace("L", "-").replace("R", "").split("\n").copy()
    else:
        out = []
        for command in in_string:
            out.append(command.replace("L", "-").replace("R", "").strip())
    return out


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
    instruction_set = create_data(in_string)
    cur_place = 50
    times_pointing_zero = 0
    for instruction in instruction_set:
        cur_place += int(instruction)
        cur_place = cur_place % 100
        if cur_place == 0:
            times_pointing_zero += 1
    return times_pointing_zero


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
    instruction_set = create_data(in_string)
    cur_place = 50
    times_pointing_zero = 0
    for instruction in instruction_set:
        cur_place += int(instruction)
        if cur_place > 0:
            times_pointing_zero += cur_place // 100
            cur_place = cur_place % 100
        elif cur_place == 0:
            times_pointing_zero += 1
        elif cur_place < 0 and int(instruction) != cur_place:
            times_pointing_zero += abs(cur_place) // 100 + 1
            cur_place = 100 - (abs(cur_place) % 100)
        else:
            times_pointing_zero += abs(cur_place) // 100
            cur_place = 100 - (abs(cur_place) % 100)
        # Strange fix for a weird error I'm having with negative
        # numbers... who knows? And I'm too tired to fix it.
        if cur_place == 100:
            cur_place = 0

    return times_pointing_zero


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
