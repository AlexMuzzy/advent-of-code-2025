from typing import List


map = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def solve_day4(input: List[str]) -> int:
    count = 0
    for i, line in enumerate(input):
        for j, c1 in enumerate(line):
            if not c1 == "@":
                continue

            paper_roll_count = 0
            for x, y in map:
                x_coords = j + x
                y_coords = i + y

                # Boundary detection
                if not y_coords > 0 or not y_coords <= len(input):
                    continue

                if not x_coords > 0 or not x_coords <= len(line):
                    continue

                current_char = input[y_coords][x_coords]
                if current_char == "@":
                    paper_roll_count += 1

            if paper_roll_count < 4:
                count += 1

    return count
