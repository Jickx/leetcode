# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements. Note that you must do this
# in-place without making a copy of the array.


def move_zeroes(nums: list[int]) -> list[int]:
    ctr = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[i], nums[ctr] = nums[ctr], nums[i]
            ctr += 1
    return nums


assert move_zeroes([0, 1, 0, 2, 3, 0, 4, 5, 6]) == [1, 2, 3, 4, 5, 6, 0, 0, 0]
assert move_zeroes([0, 0, 1]) == [1, 0, 0]
