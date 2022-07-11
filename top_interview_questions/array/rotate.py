# Given an array, rotate the array to the right by k steps,
# where k is non-negative.

from collections import deque


def rotate(nums, k):
    aux = deque(nums)
    aux.rotate(k)
    nums.clear()
    for i in aux:
        nums.append(i)
    print(nums)


rotate([1, 2, 3, 4, 5, 6, 7], 3)  # [5, 6, 7, 1, 2, 3, 4]
rotate([-1, -100, 3, 99], 2)  # [3,99,-1,-100]
rotate([1, 2], 3)  # [2, 1]
