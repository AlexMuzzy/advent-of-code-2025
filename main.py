from os import path
from solutions.day1.solution import solve


def get_file_input(day: int, part: int):
    with open(path.join("inputs", f"day{day}", f"part{part}.txt")) as f:
        return f.read().splitlines()


def main():
    day1_part1_input = get_file_input(1, 1)
    print(f"Day 1 - part 1: {solve(day1_part1_input)}")


if __name__ == "__main__":
    main()
