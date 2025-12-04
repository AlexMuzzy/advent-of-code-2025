def solve_day2_part1(input: str) -> int:
    sumOfInvalidIds = 0
    separatedList = input.split(",")

    for rangeStr in separatedList:
        (min, max) = (int(rangeStr.split("-")[0]), int(rangeStr.split("-")[1]))

        for x in range(min, max + 1):
            str1 = str(x)

            if len(str1) % 2 == 0:
                midway = (int)(len(str1) / 2)
                (str2, str3) = (str1[:midway], str1[midway:])
                if str2 == str3:
                    print(f"Invalid={x}")
                    sumOfInvalidIds = sumOfInvalidIds + x

    return sumOfInvalidIds


def solve_day2_part2(input: str) -> str:
    sum_of_invalid_ids = 0
    separated_list = input.split(",")

    for rangeStr in separated_list:
        (min_value, max_value) = (
            int(rangeStr.split("-")[0]),
            int(rangeStr.split("-")[1]),
        )

        for x in range(min_value, max_value + 1):
            str1 = str(x)
            midway = int(len(str1) / 2)
            for idx, _ in enumerate(str1[:midway]):
                str2 = str1[0 : idx + 1]
                str3 = str1[0 : idx + 1] * (len(str1) // len(str2))
                if str1 == str3:
                    print(f"Invalid={x}")
                    sum_of_invalid_ids = sum_of_invalid_ids + x
                    break

    return sum_of_invalid_ids
