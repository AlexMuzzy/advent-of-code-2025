from typing import List


def solve_day3(input: List[str], v_count: int):
    r = 0

    for s in input:
        sum_string = ""
        latest_idx = 0
        for i in range(v_count):
            j1 = "0"
            j1_idx = 0
            slice = (
                s[latest_idx + i : -v_count + (i + 1)]
                if v_count != i + 1
                else s[latest_idx + i :]
            )
            for idx, s1 in enumerate(slice):
                if int(s1) > int(j1):
                    j1 = s1
                    j1_idx = idx

            latest_idx += (
                j1_idx  # Appending the index since slices are relative to the iteration
            )
            sum_string += j1

        r += int(sum_string)

    return r
