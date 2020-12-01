from itertools import combinations

def pair_add(numlist: list[int]) -> dict:
    """
    This probably isn't the best way to do this
    """
    for pair in combinations(numlist, 2):
        yield {"sum": sum(pair), "pair": pair}

with open("input.txt") as f:
    numbers = [int(line.strip()) for line in f]

for results in pair_add(numbers):
    if results["sum"] == 2020:
        a, b = results["pair"]
        print(a, b)
        print(a * b)
