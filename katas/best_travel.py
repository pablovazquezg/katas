# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python
from typing import Optional, List
from itertools import combinations


def choose_best_sum(
    max_miles: int, max_cities: int, distances: list[int]
) -> Optional[int]:
    return max(
        (
            combo_miles
            for combo in combinations(distances, max_cities)
            if (combo_miles := sum(combo)) <= max_miles
        ),
        default=None,
    )


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(230, 4, xs))
