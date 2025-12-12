from typing import List, Tuple


map = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def solve_day4_part1(input: List[str]) -> Tuple[List[str], int]:
    count = 0
    visited_list = [list(line) for line in input]
    to_remove = []

    for i, line in enumerate(visited_list):
        for j, c1 in enumerate(line):
            if not c1 == "@":
                continue

            paper_roll_count = 0
            for x, y in map:
                x_coords = j + x
                y_coords = i + y

                # Boundary detection
                if not y_coords >= 0 or not y_coords < len(visited_list):
                    continue

                if not x_coords >= 0 or not x_coords < len(line):
                    continue

                current_char = visited_list[y_coords][x_coords]
                if current_char == "@":
                    paper_roll_count += 1

            if paper_roll_count < 4:
                to_remove.append((i, j))
                count += 1

    for i, j in to_remove:
        visited_list[i][j] = "x"

    return ["".join(line) for line in visited_list], count


def solve_day4_part2(input: List[str]) -> int:
    count = 0
    current_list = input.copy()
    while True:
        (visited_list, roll_count) = solve_day4_part1(current_list)

        if roll_count == 0:
            break

        count = count + roll_count
        current_list = visited_list

    return count
