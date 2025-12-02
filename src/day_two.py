"""
Module to solve Day 1 for Advent of Code 2025.
Author: TypeAskee
"""


def create_data(in_string: str) -> list[list[int]]:
    """
    Creates a prepared list of strings containing the commands.
    This list should only contain elements that are ready to be
    cast as strings.

    Parameters:
        in_string (str | list[str]) The input file

    Returns:
        list[str] The organized list of instructions in string form.
    """
    tmp = in_string.split(",")
    out = []
    for entry in tmp:
        tmp_two = entry.split("-")
        out.append([int(tmp_two[0]), int(tmp_two[1])])

    return out


def find_bad_id(in_num: str) -> bool:
    places = len(in_num) / 2
    if places % 1 != 0:
        return False
    places = int(places)
    test_str = in_num[:places] + in_num[:places]
    if test_str == in_num:
        return True
    return False


def find_bad_ids(in_num: str) -> bool:
    is_bad = False
    testing_places = 1
    while testing_places <= len(in_num) // 2:
        if not len(in_num) % 1 == 0:
            testing_places += 1
            continue
        test_str = ""
        for _ in range((len(in_num) // testing_places)):
            test_str += in_num[:testing_places]
        if test_str == in_num:
            is_bad = True
            break
        testing_places += 1
    return is_bad


def calc_part_a(in_string: str) -> int:
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
    bad_id_cnt = 0
    bad_id = []
    for instruction in instruction_set:
        all_nums = [str(x) for x in range(instruction[0], instruction[1] + 1)]
        for num in all_nums:
            if find_bad_id(num):
                bad_id_cnt += 1
                bad_id.append(int(num))
    return sum(bad_id)


def calc_part_b(in_string: str) -> int:
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
    bad_id_cnt = 0
    bad_id = []
    for instruction in instruction_set:
        all_nums = [str(x) for x in range(instruction[0], instruction[1] + 1)]
        for num in all_nums:
            if find_bad_ids(num):
                bad_id_cnt += 1
                bad_id.append(int(num))
    return sum(bad_id)


def main(in_string: str) -> None:
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
        all_input = f.readline()

    main(all_input)
