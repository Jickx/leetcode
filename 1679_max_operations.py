from collections import defaultdict


# def max_operations(nums, k):
#     nums_dct = defaultdict(int)
#     for i in nums:
#         nums_dct[i] += 1
#     result = 0
#     for j in nums:
#         if j < k:
#             if j != k - j:
#                 if k - j in nums_dct and nums_dct[k - j] > 0 and nums_dct[j] > 0:
#                     nums_dct[j] -= 1
#                     nums_dct[k - j] -= 1
#                     result += 1
#             else:
#                 if j in nums_dct and nums_dct[j] > 1:
#                     nums_dct[j] -= 2
#                     result += 1
#     return result

def max_operations(nums, k):
    nums.sort()

    l, r, res = 0, len(nums) - 1, 0

    while l < r:
        if nums[l] + nums[r] > k:
            r -= 1
        elif nums[l] + nums[r] < k:
            l += 1
        else:
            res += 1
            l += 1
            r -= 1
    return res


print(max_operations([1, 2, 3, 4], 5))  # 2
print(max_operations([3, 1, 3, 4, 3], 6))  # 1
print(max_operations([3, 5, 1, 5], 2))  # 0
print(max_operations([4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 2))  # 2
print(max_operations([2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2], 3))  # 4
print(max_operations([4, 4, 1, 3, 1, 3, 2, 2, 5, 5, 1, 5, 2, 1, 2, 3, 5, 4], 2))  # 2
