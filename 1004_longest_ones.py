def longest_ones(nums, k):
    l = 0
    r = 0
    max_window = 0
    while r < len(nums):
        while nums[r] == 1:
            r += 1
        if k > 0:
            r += 1
            k -= 1
        else:
            max_window = max(max_window, r - l)

    return max_window




print(longest_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))  # 6
