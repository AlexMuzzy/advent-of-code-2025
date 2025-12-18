from typing import Dict, List


def tranpose_cols_to_rows(input: List[str]) -> List[str]:
    if not input:
        return []

    num_cols = len(input[0].split())
    output = [[] for _ in range(num_cols)]

    for _, i in enumerate(input):
        l1 = i.split()
        for idx2, j in enumerate(l1):
            output[idx2].append(j)

    return output


def transpose_col_values_to_row_values(input: List[str]) -> List[str]:
    row_input = tranpose_cols_to_rows(input)
    output = []
    num_problems = len(row_input)
    is_forward = (num_problems % 2 == 1)
    for i in row_input:
        map: Dict[int, str] = {}
        for j in i[:-1]:
            for idx, k in enumerate(j if is_forward else reversed(j)):
                if idx in map:
                    map[idx] = map[idx] + k
                else:
                    map[idx] = k

        is_forward = not is_forward
        print(f"map: {map} is_forward: {is_forward} i: {i}")
        output.append(list(map.values()) + [i[-1]])

    return output


def compute_line(line: List[str]) -> int:
    result = int(line.pop(0))
    operation_type = line.pop()
    for value in line:
        if operation_type == "*":
            result *= int(value)
        elif operation_type == "+":
            result += int(value)

    return result


def solve_day6_part1(input: List[str]) -> int:
    return sum(compute_line(line) for line in tranpose_cols_to_rows(input))


def solve_day6_part2(input: List[str]) -> int:
    return sum(compute_line(line) for line in transpose_col_values_to_row_values(input))
