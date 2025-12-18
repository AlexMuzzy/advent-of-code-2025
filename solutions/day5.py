from typing import List


def solve_day5_part1(input: List[str]) -> int:
    separator_idx = input.index("")
    fresh_count = 0

    fresh_ids = [tuple(map(int, line.split("-"))) for line in input[:separator_idx]]
    ingredient_ids = [int(line) for line in input[separator_idx + 1 :] if line]

    for ingredient_id in ingredient_ids:
        for min_value, max_value in fresh_ids:
            if ingredient_id >= min_value and ingredient_id <= max_value:
                fresh_count = fresh_count + 1
                break

    return fresh_count


def solve_day5_part2(input: List[str]) -> int:
    separator_idx = input.index("")

    fresh_ids = [tuple(map(int, line.split("-"))) for line in input[:separator_idx]]
    fresh_ids.sort()

    merged = []
    for start, end in fresh_ids:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    fresh_count = sum(end - start + 1 for start, end in merged)
    return fresh_count
