from os import path
from typing import Optional
from solutions.day1.solution import solveDay1
from solutions.day2.solution import solveDay2


def get_file_input_by_lines(day: int, part: int, is_sample: Optional[bool] = False):
    with open(
        path.join(
            "inputs", f"day{day}", f"part{part}{'-sample' if is_sample else ''}.txt"
        )
    ) as f:
        return f.read().splitlines()


def main():
    day1_input = get_file_input_by_lines(1, 1)
    day1_sample_input = get_file_input_by_lines(1, 1, True)
    print(f"Day 1 - part 1: {solveDay1(day1_input)}")
    print(f"Day 1 - part 1 - sample: {solveDay1(day1_sample_input)}")

    print(f"Day 1 - part 2: {solveDay1(day1_input, True)}")
    print(f"Day 1 - part 2 - sample: {solveDay1(day1_sample_input, True)}")

    day2_input = get_file_input_by_lines(2, 1)[0]
    day2_sample_input = get_file_input_by_lines(2, 1, True)[0]
    print(f"Day 2 - part 1: {solveDay2(day2_input)}")
    print(f"Day 2 - part 1 - sample: {solveDay2(day2_sample_input)}")


if __name__ == "__main__":
    main()
