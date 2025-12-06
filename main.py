from os import path
from typing import Optional
from solutions.day1.solution import solve_day1
from solutions.day2.solution import solve_day2_part2, solve_day2_part1
from solutions.day3.solution import solve_day3


def get_file_input_by_lines(day: int, part: int, is_sample: Optional[bool] = False):
    with open(
        path.join(
            "inputs", f"day{day}", f"part{part}{'-sample' if is_sample else ''}.txt"
        ),
        "r",
        encoding="utf-8",
    ) as f:
        return f.read().splitlines()


def main():
    day1_input = get_file_input_by_lines(1, 1)
    day1_sample_input = get_file_input_by_lines(1, 1, True)
    print(f"Day 1 - part 1: {solve_day1(day1_input)}")
    print(f"Day 1 - part 1 - sample: {solve_day1(day1_sample_input)}")

    print(f"Day 1 - part 2: {solve_day1(day1_input, True)}")
    print(f"Day 1 - part 2 - sample: {solve_day1(day1_sample_input, True)}")

    day2_input = get_file_input_by_lines(2, 1)[0]
    day2_sample_input = get_file_input_by_lines(2, 1, True)[0]
    print(f"Day 2 - part 1: {solve_day2_part1(day2_input)}")
    print(f"Day 2 - part 1 - sample: {solve_day2_part1(day2_sample_input)}")

    print(f"Day 2 - part 2: {solve_day2_part2(day2_input)}")
    print(f"Day 2 - part 2 - sample: {solve_day2_part2(day2_sample_input)}")

    day3_input = get_file_input_by_lines(3, 1)
    day3_sample_input = get_file_input_by_lines(3, 1, True)
    print(f"Day 3 - part 1: {solve_day3(day3_input, 2)}")
    print(f"Day 3 - part 1 - sample: {solve_day3(day3_sample_input, 2)}")

    print(f"Day 3 - part 2: {solve_day3(day3_input, 12)}")
    print(f"Day 3 - part 2 - sample: {solve_day3(day3_sample_input, 12)}")


if __name__ == "__main__":
    main()
