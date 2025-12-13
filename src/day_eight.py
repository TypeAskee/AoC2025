"""
Module to solve Day 8 for Advent of Code 2025.
Author: TypeAskee
"""

import math

import numpy as np


class Point:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


class DistanceMap:
    def __init__(self, axis: list[Point]):
        self.map = []
        self.npmap = np.zeros(0)
        self.axis = axis

    def calc_map(self):
        for x in self.axis:
            line = []
            for y in self.axis:
                line.append(calc_distance(x, y))
            self.map.append(line)

        self.npmap = np.array(self.map)
        self.npmap[self.npmap == 0] = 100000000000000000000000000000


def calc_distance(first: Point, second: Point) -> float:
    tmp = (first.x - second.x) ** 2
    tmp += (first.y - second.y) ** 2
    tmp += (first.z - second.z) ** 2
    return math.sqrt(tmp)


def format_lines(in_string: list[str]) -> list[Point]:
    points = []
    for line in in_string:
        tmp = line.strip().split(",")
        points.append(Point(int(tmp[0]), int(tmp[1]), int(tmp[2])))

    return points


def val_in_dict_list(in_list: dict, val):
    for key in in_list.keys():
        if val in in_list[key]:
            return key
    return None


def calc_part_a(in_string: list[str]) -> int:
    """
    Calculate part A solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
    PAIRS_TO_JOIN = 10
    points = format_lines(in_string)
    dist_map = DistanceMap(points)
    dist_map.calc_map()

    connected_pts = {}
    cnt = 0
    while cnt < PAIRS_TO_JOIN:
        indices = np.unravel_index(np.argmin(dist_map.npmap), dist_map.npmap.shape)
        if dist_map.axis[indices[0]] in connected_pts.keys():
            if (
                dist_map.axis[indices[1]]
                not in connected_pts[dist_map.axis[indices[0]]]
            ):
                connected_pts[dist_map.axis[indices[0]]].append(
                    dist_map.axis[indices[1]]
                )
        elif dist_map.axis[indices[1]] in connected_pts.keys():
            if (
                dist_map.axis[indices[0]]
                not in connected_pts[dist_map.axis[indices[1]]]
            ):
                connected_pts[dist_map.axis[indices[1]]].append(
                    dist_map.axis[indices[0]]
                )
        elif val_in_dict_list(connected_pts, dist_map.axis[indices[0]]):
            key = val_in_dict_list(connected_pts, dist_map.axis[indices[0]])
            connected_pts[key].append(dist_map.axis[indices[1]])
        elif val_in_dict_list(connected_pts, dist_map.axis[indices[1]]):
            key = val_in_dict_list(connected_pts, dist_map.axis[indices[1]])
            connected_pts[key].append(dist_map.axis[indices[0]])
        else:
            connected_pts[dist_map.axis[indices[0]]] = [dist_map.axis[indices[1]]]
        cnt += 1
        dist_map.npmap[indices] = 1000000000000000000
        dist_map.npmap[(indices[1], indices[0])] = 100000000000000

    lengths = []
    for key in connected_pts.keys():
        lengths.append(len(connected_pts[key]))

    lengths = sorted(lengths, reverse=True)

    return (lengths[0] + 1) * (lengths[1] + 1) * (lengths[2] + 1)


def calc_part_b(in_string: list[str]) -> int:
    """
    Calculate part B solution!

    Parameters:
        in_string (list[str]) The list of instructions.

    Results:
        int The solution to the puzzle!
    """
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
