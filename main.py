from os import path
from time import time
from typing import Callable, Optional

from solutions.day1 import solve_day1
from solutions.day2 import solve_day2_part1, solve_day2_part2
from solutions.day3 import solve_day3
from solutions.day4 import solve_day4_part1, solve_day4_part2
from solutions.day5 import solve_day5_part1, solve_day5_part2
from solutions.day6 import solve_day6_part1, solve_day6_part2
from solutions.day7 import solve_day7_part1, solve_day7_part2


def print_and_measure(func: Callable, day: int, part: int, *args, **kwargs):
    start_time = time()
    result = func(*args, **kwargs)
    end_time = time()
    print(f"Day {day} - part {part}: {result} ({end_time - start_time:.6f}s)")


def get_file_input_by_lines(day: int, is_sample: Optional[bool] = False):
    with open(
        path.join("inputs", f"day{day}", f"{'sample' if is_sample else 'data'}.txt"),
        "r",
        encoding="utf-8",
    ) as f:
        return f.read().splitlines()


def main():
    day1_input = get_file_input_by_lines(1)
    day1_sample_input = get_file_input_by_lines(1, True)
    print_and_measure(solve_day1, 1, 1, day1_input)
    print_and_measure(solve_day1, 1, 1, day1_sample_input)

    print_and_measure(solve_day1, 1, 2, day1_input, True)
    print_and_measure(solve_day1, 1, 2, day1_sample_input, True)

    day2_input = get_file_input_by_lines(2)[0]
    day2_sample_input = get_file_input_by_lines(2, True)[0]
    print_and_measure(solve_day2_part1, 2, 1, day2_input)
    print_and_measure(solve_day2_part1, 2, 1, day2_sample_input)

    print_and_measure(solve_day2_part2, 2, 2, day2_input)
    print_and_measure(solve_day2_part2, 2, 2, day2_sample_input)

    day3_input = get_file_input_by_lines(3)
    day3_sample_input = get_file_input_by_lines(3, True)
    print_and_measure(solve_day3, 3, 1, day3_input, 2)
    print_and_measure(solve_day3, 3, 1, day3_sample_input, 2)

    print_and_measure(solve_day3, 3, 2, day3_input, 12)
    print_and_measure(solve_day3, 3, 2, day3_sample_input, 12)

    day4_input = get_file_input_by_lines(4)
    day4_sample_input = get_file_input_by_lines(4, True)
    print_and_measure(solve_day4_part1, 4, 1, day4_input)
    print_and_measure(solve_day4_part1, 4, 1, day4_sample_input)

    day4_input = get_file_input_by_lines(4)
    day4_sample_input = get_file_input_by_lines(4, True)
    print_and_measure(solve_day4_part2, 4, 2, day4_input)
    print_and_measure(solve_day4_part2, 4, 2, day4_sample_input)

    day5_input = get_file_input_by_lines(5)
    day5_sample_input = get_file_input_by_lines(5, True)
    print_and_measure(solve_day5_part1, 5, 1, day5_input)
    print_and_measure(solve_day5_part1, 5, 1, day5_sample_input)

    print_and_measure(solve_day5_part2, 5, 2, day5_input)
    print_and_measure(solve_day5_part2, 5, 2, day5_sample_input)

    day6_input = get_file_input_by_lines(6)
    day6_sample_input = get_file_input_by_lines(6, True)
    print_and_measure(solve_day6_part1, 6, 1, day6_input)
    print_and_measure(solve_day6_part1, 6, 1, day6_sample_input)

    print_and_measure(solve_day6_part2, 6, 2, day6_input)
    print_and_measure(solve_day6_part2, 6, 2, day6_sample_input)

    day7_input = get_file_input_by_lines(7)
    day7_sample_input = get_file_input_by_lines(7, True)
    print_and_measure(solve_day7_part1, 7, 1, day7_input)
    print_and_measure(solve_day7_part1, 7, 1, day7_sample_input)

    print_and_measure(solve_day7_part2, 7, 2, day7_input)
    print_and_measure(solve_day7_part2, 7, 2, day7_sample_input)


if __name__ == "__main__":
    main()
