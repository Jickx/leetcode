def single_number(nums: list[int]) -> int:
    while nums:
        el = nums.pop()
        if el in nums:
            continue
        else:
            return el


assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([1]) == 1
