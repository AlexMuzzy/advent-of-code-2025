from os import path
from typing import Optional
from solutions.day1.solution import solve


def get_file_input(day: int, part: int, is_sample: Optional[bool] = False):
    with open(
        path.join(
            "inputs", f"day{day}", f"part{part}{'-sample' if is_sample else ''}.txt"
        ),
        "r",
        encoding="utf-8",
    ) as f:
        return f.read().splitlines()


def main():
    day1_input = get_file_input(1, 1)
    day1_sample_input = get_file_input(1, 1, True)
    print(f"Day 1 - part 1: {solve(day1_input)}")
    print(f"Day 1 - part 1 - sample: {solve(day1_sample_input)}")

    print(f"Day 1 - part 2: {solve(day1_input, True)}")
    print(f"Day 1 - part 2 - sample: {solve(day1_sample_input, True)}")


if __name__ == "__main__":
    main()
