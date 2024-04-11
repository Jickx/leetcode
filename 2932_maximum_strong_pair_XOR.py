def maximum_strong_pair_Xor(nums: list[int]) -> int:
    nums_set = set()
    for i in nums:
        for j in nums:
            if abs(i - j) <= min(i, j):
                nums_set.add(tuple(sorted([i, j])))
    result = 0
    for a, b in nums_set:
        result = max(result, a ^ b)

    return result


print(maximum_strong_pair_Xor([1, 2, 3, 4, 5]))  # 7
print(maximum_strong_pair_Xor([5, 6, 25, 30]))  # 7
print(maximum_strong_pair_Xor([10, 100]))  # 0
