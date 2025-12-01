from typing import List


def compute_left(amount: int, val: int) -> int:
    if amount > val:
        result = 100 - (amount - val) % 100

        if result == 100:
            return 0
        return result
    else:
        return val - amount


def compute_right(amount: int, val: int) -> int:
    if amount + val > 99:
        return (amount + val) % 100

    else:
        return val + amount


def compute_amount(direction: str, amount: int, val: int) -> int:
    if direction == "L":
        return compute_left(amount, val)

    if direction == "R":
        return compute_right(amount, val)


def solve(input: List[str]) -> int:
    val = 50
    count = 0

    for combination in input:
        (direction, amount) = (combination[:1], int(combination[1:]))
        val = compute_amount(direction, amount, val)

        print(f"Key={combination} Value={val} {'Bug!' if val == 100 else ''}")

        if val == 0:
            count += 1

    return count
