from itertools import combinations
from functools import reduce
from typing import List

import adventinput


def ntuple_add(numlist: List[int], tuple_size: int) -> dict:
    """
    This probably isn't the best way to do this
    """
    for n_tuple in combinations(numlist, tuple_size):
        yield {"sum": sum(n_tuple), "tuple": n_tuple}


def get_results(numlist: List[int], tuple_size: int):
    for results in ntuple_add(numlist, tuple_size):
        if results["sum"] == 2020:
            print(results["tuple"])
            print(reduce(lambda x, y: x * y, results["tuple"]))
            break


numbers = [int(i) for i in adventinput.get_data(1)]

get_results(numbers, 2)
get_results(numbers, 3)
