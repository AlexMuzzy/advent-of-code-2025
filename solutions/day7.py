from functools import lru_cache
from typing import List, Set, Tuple


def traverse_beam(
    input: List[str], beams: Set[Tuple[int, int]], coords: Tuple[int, int], count: int
) -> int:
    (x, y) = coords
    for idx, line in enumerate(input[x:]):
        current_char = line[y]
        current_x = x + idx
        if current_char == "^":
            coords1 = current_x, y - 1
            coords2 = current_x, y + 1
            split_performed = False

            if coords1 not in beams:
                split_performed = True
                beams.add(coords1)
                count = traverse_beam(input, beams, coords1, count)

            if coords2 not in beams:
                split_performed = True
                beams.add(coords2)
                count = traverse_beam(input, beams, coords2, count)

            # This accounts for the edge case where a splitter could be hit but both splits have already been traversed.
            if split_performed:
                count = count + 1

            # Beam has now been split
            break

    return count


def solve_day7_part1(input: List[str]) -> int:
    # Figure out location of starting value
    beams: Set[Tuple[int, int]] = set()
    count = 0

    coords = 0, input[0].index("S")
    beams.add(coords)

    count = traverse_beam(input, beams, coords, count)

    return count


def solve_day7_part2(input: List[str]) -> int:
    # Figure out location of starting value
    x, y = 0, input[0].index("S")

    @lru_cache(None)
    def traverse_beam_by_path(x: int, y: int) -> int:
        for idx, line in enumerate(input[x:]):
            current_char = line[y]
            current_x = x + idx
            if current_char == "^":
                return traverse_beam_by_path(current_x, y - 1) + traverse_beam_by_path(
                    current_x, y + 1
                )

        return 1

    count = traverse_beam_by_path(x, y)

    return count
