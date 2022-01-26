from math import ceil
from typing import List


def even_and_odd_to(i):
    # even numbers
    a = [x * 2 for x in range(i)]
    # odd numbers
    b = [x + 1 for x in a]
    return a, b

def make_even_blocks(i, relation):
    half = ceil(i / 2)
    a, b = even_and_odd_to(half)
    return merge_while([], a, b, relation)


def merge_while(res: List[int], a: List[int], b: List[int], relation: int)\
        -> List[int]:
    while(len(a) >= relation):
        res.extend(a[0:relation])
        tmp = b
        b = a[relation:]
        a = tmp
    res.extend(b)
    res.extend(a)
    return res

def distribute_even(target_len, rel):
    # rel is ment as in % case
    # i.e. for rel = 5, the relation will be 1 True : 4 False
    half =ceil(target_len/2)
    uneven, even = 1, 2
    fst_half, scnd_half = even_and_odd_to(half)
    for i in range(1, half+1):
        if i % rel == 0:
            tmp = fst_half[i-1]
            fst_half[i-1] = scnd_half[i-1]
            scnd_half[i-1] = tmp
    return fst_half+scnd_half
