# Given a non-empty array of integers nums, every element appears twice except
# for one. Find that single one. You must implement a solution with a linear
# runtime complexity and use only constant extra space.

from collections import Counter


def single_number(nums: list[int]) -> int:
    ctr = Counter(nums)
    for k, v in dict(ctr).items():
        if v == 1:
            return k


assert single_number([2, 2, 1]) == 1
assert single_number([4, 1, 2, 1, 2]) == 4
assert single_number([1]) == 1
