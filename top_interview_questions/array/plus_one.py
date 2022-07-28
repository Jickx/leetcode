def plus_one(digits: list[int]) -> list[int]:
    number = int(''.join(str(i) for i in digits)) + 1
    return [int(i) for i in str(number)]


assert plus_one([1, 9]) == [2, 0]
assert plus_one([1, 9, 9, 9, 9, 9, 9, 9]) == [2, 0, 0, 0, 0, 0, 0, 0]
assert plus_one([4, 3, 2, 1]) == [4, 3, 2, 2]
assert plus_one([9]) == [1, 0]
