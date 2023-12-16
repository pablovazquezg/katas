# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python

import math


def persistence(num: int) -> int:
    if num < 10:
        return 0

    digits = [int(d) for d in str(num)]
    return persistence(math.prod(digits)) + 1
