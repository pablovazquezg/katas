# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python
from typing import Optional
from itertools import combinations


def choose_best_sum(max_miles: int, max_cities: int, distances: int) -> Optional[int]:
    options = [
        sum(miles)
        for miles in combinations(distances, max_cities)
        if sum(miles) <= max_miles
    ]

    return max(options, default=None)


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
choose_best_sum(230, 4, xs)
