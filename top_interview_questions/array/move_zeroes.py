# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements. Note that you must do this
# in-place without making a copy of the array.


def move_zeroes(nums: list[int]) -> list[int]:
    count_zero = nums.count(0)
    for i in range(count_zero):
        nums.remove(0)
        nums.append(0)
    return nums


print(move_zeroes([0, 1, 0, 2, 3, 0, 4, 5, 6]))
print(move_zeroes([0, 0, 1]))
