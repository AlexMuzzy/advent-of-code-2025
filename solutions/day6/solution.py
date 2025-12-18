from typing import Dict, List, Tuple


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


def transpose_cols_to_rows_with_direction(input: List[str]) -> List[Tuple[List[str], bool]]:
    if not input:
        return []

    # Find column start positions from operator row
    operator_row = input[-1]
    col_starts = [i for i, c in enumerate(operator_row) if c in '+*']

    result = []
    for i, start in enumerate(col_starts):
        end = col_starts[i + 1] if i + 1 < len(col_starts) else len(operator_row)
        values = []
        is_left_padded = False

        for line in input:
            slot = line[start:end]
            values.append(slot.strip())
            # Check if number row has leading space
            if slot[0] == ' ' and slot.strip() not in '+-*/':
                is_left_padded = True

        result.append((values, not is_left_padded))

    return result


def transpose_col_values_to_row_values(input: List[str]) -> List[str]:
    row_input = transpose_cols_to_rows_with_direction(input)
    output = []
    for values, is_forward in row_input:
        map: Dict[int, str] = {}
        for j in values[:-1]:  # All values except the operator
            for idx, k in enumerate(j if is_forward else reversed(j)):
                if idx in map:
                    map[idx] = map[idx] + k
                else:
                    map[idx] = k

        print(f"map: {map} is_forward: {is_forward} values: {values}")
        output.append(list(map.values()) + [values[-1]])  # Append operator

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
