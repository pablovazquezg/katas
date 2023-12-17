# https://www.codewars.com/kata/58925dcb71f43f30cd00005f

from itertools import permutations


def late_clock(a, b, c, d):
    times = sorted(permutations([a, b, c, d]), reverse=True)

    for time in times:
        h1, h2, m1, m2 = time[0], time[1], time[2], time[3]
        if h1 * 10 + h2 < 24 and m1 < 6:  # valid time?
            return f"{h1}{h2}:{m1}{m2}"  # return first valid


# Test the function
print(late_clock(1, 9, 8, 3))  # Output: "19:38"
print(late_clock(9, 1, 2, 5))  # Output: "21:59"
print(late_clock(0, 0, 0, 0))  # Output: "00:00"
print(late_clock(2, 3, 5, 8))  # Output: "23:58"
