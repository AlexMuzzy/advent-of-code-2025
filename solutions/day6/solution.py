from typing import List


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


def solve_day6_part1(input: List[str]) -> int:
    transposed_input = tranpose_cols_to_rows(input)

    def compute_line(line: List[str]) -> int:
        result = int(line.pop(0))
        operation_type = line.pop()
        for value in line:
            if operation_type == "*":
                result *= int(value)
            elif operation_type == "+":
                result += int(value)

        return result

    return sum(compute_line(line) for line in transposed_input)
