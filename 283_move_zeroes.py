def move_zeroes(nums):
    ctr = 0
    for i in range(len(nums)):
        if nums[i]:
            nums[i], nums[ctr] = nums[ctr], nums[i]
            ctr += 1
    return nums


print(move_zeroes([1, 0, 1]))  # [1, 1, 0]
print(move_zeroes([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
print(move_zeroes([0, 0, 1]))  # [1, 0, 0]
print(move_zeroes([2, 1]))  # [2, 1]
