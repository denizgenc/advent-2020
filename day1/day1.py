from itertools import combinations
from functools import reduce

def ntuple_add(numlist: list[int], tuple_size: int) -> dict:
    """
    This probably isn't the best way to do this
    """
    for n_tuple in combinations(numlist, tuple_size):
        yield {"sum": sum(n_tuple), "tuple": n_tuple}

def get_results(numlist: list[int], tuple_size: int):
    for results in ntuple_add(numlist, tuple_size):
        if results["sum"] == 2020:
            print(results["tuple"])
            print(reduce(lambda x, y: x * y, results["tuple"]))
            break


with open("input.txt") as f:
    numbers = [int(line.strip()) for line in f]

get_results(numbers, 2)
get_results(numbers, 3)
