def plus_one(digits: list[int]) -> list[int]:
    digits[-1] += 1
    for i in range(len(digits) - 1, 0, -1):
        if digits[i] == 10:
            digits[i] = 0
            digits[i - 1] += 1
    return digits


assert plus_one([1, 9]) == [2, 0]
assert plus_one([1, 9, 9, 9, 9, 9, 9, 9]) == [2, 0, 0, 0, 0, 0, 0, 0]
assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
