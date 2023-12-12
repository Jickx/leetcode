# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def remove_duplicates(nums):
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            del nums[i]
        else:
            i += 1
    return len(nums)


assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
assert remove_duplicates([1, 1, 2]) == 2
