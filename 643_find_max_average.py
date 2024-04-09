def find_max_average(nums, k):
    l = 0
    r = k
    max_s = s = sum(nums[l:r])
    while l + k < len(nums):
        s -= nums[l]
        s += nums[r]
        if s > max_s:
            max_s = s
        l += 1
        r += 1
    return max_s / k


print(find_max_average([3, 1, 12, -5, -6, 50], 4))  # 12.75000
print(find_max_average([5], 1))  # 5
