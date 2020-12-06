from functools import reduce
from typing import List

import adventinput


def count_trees(forest_map: List[str], x_speed: int, y_speed: int) -> int:
    """
    Count the amount of trees encountered in the forest map for a toboggan moving
    x_speed squares to the right for y_speed squares downwards.

    forest_map is a list of strings, where . represents an open space and # represents
    a tree.
    """
    width = len(forest_map[0])
    tree_count = 0
    x_pos = 0
    for y_pos in range(y_speed, len(forest_map), y_speed):
        x_pos = (x_pos + x_speed) % width
        tree_count += 1 if forest_map[y_pos][x_pos] == "#" else 0
    return tree_count


forest_map = adventinput.get_data(3)

part1_answer = count_trees(forest_map, 3, 1)
print(f"The part 1 answer is {part1_answer}")
slopes = [
    part1_answer,
    count_trees(forest_map, 1, 1),
    count_trees(forest_map, 5, 1),
    count_trees(forest_map, 7, 1),
    count_trees(forest_map, 1, 2),
]
part2_answer = reduce(lambda x, y: x * y, slopes)
print(f"The part 2 answer is {part2_answer}")
