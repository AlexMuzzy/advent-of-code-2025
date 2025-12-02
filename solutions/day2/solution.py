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
