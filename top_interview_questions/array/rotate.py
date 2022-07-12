# Given an array, rotate the array to the right by k steps,
# where k is non-negative.

def rotate(nums, k):
    for i in range(k):
        nums.insert(0, nums.pop())
    return nums


assert rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
assert rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
assert rotate([1, 2], 3) == [2, 1]
