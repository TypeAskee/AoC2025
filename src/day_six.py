"""
Module to solve Day 6 for Advent of Code 2025.
Author: TypeAskee
"""

import re


def format_lines(in_string: list[str]):
    nums_to_operate = []
    for line in in_string[:-1]:
        tmp = re.sub(r"\s+", ",", line.strip())
        tmp = tmp.split(",")
        nums_to_operate.append(tmp)

    operations = re.sub(r"\s+", ",", in_string[-1].strip()).split(",")
    return nums_to_operate, operations


def format_lines_b(in_string: list[str]):
    nums_to_operate = []
    col_indices = [i - 1 for i, x in enumerate(in_string[-1].strip()) if x != " "]
    col_indices.pop(0)
    col_orig_nums = []
    for line in in_string[:-1]:
        for idx in col_indices:
            line = line[:idx] + "," + line[idx + 1 :]
        col_orig_nums.append(line.strip().split(","))

    re_org = []
    for x in range(len(col_orig_nums[0])):
        re_org_sub = []
        for y in range(len(col_orig_nums)):
            re_org_sub.append(col_orig_nums[y][x])
        re_org.append(re_org_sub)

    # fix for beginning of line
    tmp = re_org[0]
    max_size = len(max(tmp, key=len))
    for idx in range(len(tmp)):
        val = tmp[idx]
        while len(val) != max_size:
            val = " " + val
        tmp[idx] = val

    # fix for end of line
    tmp = re_org[-1]
    max_size = len(max(tmp, key=len))
    for idx in range(len(tmp)):
        val = tmp[idx]
        while len(val) != max_size:
            val = val + " "
        tmp[idx] = val

    # rotation
    for idx, nums in enumerate(re_org):
        new_nums = []
        max_size = len(max(nums, key=len))
        for x in range(max_size):
            new_num = ""
            for y in range(len(nums)):
                new_num += nums[y][x - max_size]
            new_nums.append(int(new_num))
        nums_to_operate.append(new_nums)

    operations = re.sub(r"\s+", ",", in_string[-1].strip()).split(",")
    return nums_to_operate, operations


def operate(x: str | int, y: str | int, operation: str) -> int:
    if operation == "*":
        result = int(x) * int(y)
    else:
        result = int(x) + int(y)
    return result


def calc_part_a(in_string: list[str]) -> int:
    """
    Calculate part A solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    nums, operations = format_lines(in_string)
    final_result = 0
    for idx, operation in enumerate(operations):
        if operation == "*":
            result = 1
        else:
            result = 0
        for num in nums:
            result = operate(result, num[idx], operation)
        final_result += result

    return final_result


def calc_part_b(in_string: list[str]) -> int:
    """
    Calculate part B solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    nums, operations = format_lines_b(in_string)
    final_result = 0
    for idx, operation in enumerate(operations):
        if operation == "*":
            result = 1
            for num in nums[idx]:
                result *= num
        else:
            result = 0
            for num in nums[idx]:
                result += num
        final_result += result

    return final_result


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
