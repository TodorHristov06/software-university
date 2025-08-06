from itertools import permutations

def possible_permutations(lst):
    for perm in permutations(lst):
        yield list(perm)
