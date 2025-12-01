import math
from typing import List, Tuple


def compute_left(amount: int, val: int) -> Tuple[int]:
    if not amount > val:
        return (val - amount, 0)

    calc = 100 - (amount - val)
    result = calc % 100

    if result == 100:
        return 0

    count = math.ceil(calc / 100)

    return (result, count)


def compute_right(amount: int, val: int) -> Tuple[int]:
    if not amount + val > 99:
        return (val + amount, 0)

    calc = amount + val
    result = calc % 100

    count = math.floor(calc / 100)

    return (result, count)


def compute_amount(
    direction: str, amount: int, val: int, count_ticks: bool = False
) -> Tuple[int]:
    count = 0
    if direction == "L":
        (result, calc) = compute_left(amount, val)

    if direction == "R":
        (result, calc) = compute_right(amount, val)

    if not count_ticks:
        calc = 1 if result == 0 else 0

    count += calc
    return (result, count)


def solve(input: List[str], count_ticks: bool = False) -> int:
    val = 50
    count = 0

    for combination in input:
        (direction, amount) = (combination[:1], int(combination[1:]))
        (val1, count1) = compute_amount(direction, amount, val, count_ticks)
        val = val1
        count = count + count1

        print(f"(Key={combination} Value={val} Count={count})")

    return count
