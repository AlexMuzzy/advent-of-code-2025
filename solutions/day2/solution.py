def solveDay2(input: str) -> int:
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

    print(sumOfInvalidIds)
    return sumOfInvalidIds


def solve_day2_part2(input: str) -> str:
    sumOfInvalidIds = 0
    separatedList = input.split(",")

    for rangeStr in separatedList:
        (min, max) = (int(rangeStr.split("-")[0]), int(rangeStr.split("-")[1]))

        for x in range(min, max + 1):
            str1 = str(x)
            # 0/1
            # 0-1/2-3
            # 0-2/3-5
            # 0-3/4-7
            if len(str1) % 2 == 0:
                midway = (int)(len(str1) / 2)
                for idx, _ in enumerate(str1[:midway]):
                    str2 = str1[0 : idx + 1]
                    str3 = str1[idx + 1 : (idx * 2) + 2]
                    if str2 == str3:
                        print(f"Invalid={x}")
                        sumOfInvalidIds = sumOfInvalidIds + x
                    str2 = str1[0 : idx + 1]
                    str3 = str1[0 : idx + 1]

    print(sumOfInvalidIds)
    return sumOfInvalidIds
