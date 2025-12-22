from typing import List, Set, Tuple


def traverse_beam(
    input: List[str], beams: Set[Tuple[int, int]], coords: Tuple[int, int], count: int
) -> int:
    (x, y) = coords
    for idx, line in enumerate(input[x + 1 :]):
        current_char = line[y]
        print(f"x={x + idx} y={y} current_char={current_char}")
        if current_char == "^":
            coords1 = idx, y - 1
            coords2 = idx, y + 1
            count = count + 1

            if coords1 not in beams:
                beams.add(coords1)
                count = traverse_beam(input, beams, coords1, count)

            if coords2 not in beams:
                beams.add(coords2)
                count = traverse_beam(input, beams, coords2, count)

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
