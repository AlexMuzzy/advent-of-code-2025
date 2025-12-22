from os import path
from typing import Optional

from solutions.day1 import solve_day1
from solutions.day2 import solve_day2_part1, solve_day2_part2
from solutions.day3 import solve_day3
from solutions.day4 import solve_day4_part1, solve_day4_part2
from solutions.day5 import solve_day5_part1, solve_day5_part2
from solutions.day6 import solve_day6_part1, solve_day6_part2
from solutions.day7 import solve_day7_part1


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
    print(f"Day 1 - part 1: {solve_day1(day1_input)}")
    print(f"Day 1 - part 1 - sample: {solve_day1(day1_sample_input)}")

    print(f"Day 1 - part 2: {solve_day1(day1_input, True)}")
    print(f"Day 1 - part 2 - sample: {solve_day1(day1_sample_input, True)}")

    day2_input = get_file_input_by_lines(2)[0]
    day2_sample_input = get_file_input_by_lines(2, True)[0]
    print(f"Day 2 - part 1: {solve_day2_part1(day2_input)}")
    print(f"Day 2 - part 1 - sample: {solve_day2_part1(day2_sample_input)}")

    print(f"Day 2 - part 2: {solve_day2_part2(day2_input)}")
    print(f"Day 2 - part 2 - sample: {solve_day2_part2(day2_sample_input)}")

    day3_input = get_file_input_by_lines(3)
    day3_sample_input = get_file_input_by_lines(3, True)
    print(f"Day 3 - part 1: {solve_day3(day3_input, 2)}")
    print(f"Day 3 - part 1 - sample: {solve_day3(day3_sample_input, 2)}")

    print(f"Day 3 - part 2: {solve_day3(day3_input, 12)}")
    print(f"Day 3 - part 2 - sample: {solve_day3(day3_sample_input, 12)}")

    day4_input = get_file_input_by_lines(4)
    day4_sample_input = get_file_input_by_lines(4, True)
    (_, day4_result) = solve_day4_part1(day4_input)
    (_, day4_sample_result) = solve_day4_part1(day4_sample_input)
    print(f"Day 4 - part 1: {day4_result}")
    print(f"Day 4 - part 1 - sample: {day4_sample_result}")

    day4_input = get_file_input_by_lines(4)
    day4_sample_input = get_file_input_by_lines(4, True)
    print(f"Day 4 - part 2: {solve_day4_part2(day4_input)}")
    print(f"Day 4 - part 2 - sample: {solve_day4_part2(day4_sample_input)}")

    day5_input = get_file_input_by_lines(5)
    day5_sample_input = get_file_input_by_lines(5, True)
    print(f"Day 5 - part 1: {solve_day5_part1(day5_input)}")
    print(f"Day 5 - part 1 - sample: {solve_day5_part1(day5_sample_input)}")

    print(f"Day 5 - part 2: {solve_day5_part2(day5_input)}")
    print(f"Day 5 - part 2 - sample: {solve_day5_part2(day5_sample_input)}")

    day6_input = get_file_input_by_lines(6)
    day6_sample_input = get_file_input_by_lines(6, True)
    print(f"Day 6 - part 1: {solve_day6_part1(day6_input)}")
    print(f"Day 6 - part 1 - sample: {solve_day6_part1(day6_sample_input)}")

    print(f"Day 6 - part 2: {solve_day6_part2(day6_input)}")
    print(f"Day 6 - part 2 - sample: {solve_day6_part2(day6_sample_input)}")

    day7_input = get_file_input_by_lines(7)
    day7_sample_input = get_file_input_by_lines(7, True)
    # print(f"Day 7 - part 1: {solve_day7_part1(day7_input)}")
    print(f"Day 7 - part 1 - sample: {solve_day7_part1(day7_sample_input)}")


if __name__ == "__main__":
    main()
