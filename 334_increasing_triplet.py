def increasing_triplet(nums):
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False


print(increasing_triplet([1, 2, 3, 4, 5]))  # True
print(increasing_triplet([5, 4, 3, 2, 1]))  # False
print(increasing_triplet([2, 1, 5, 0, 4, 6]))  # True
print(increasing_triplet([2, 0, 6, 1, 4, 6]))  # True
print(increasing_triplet([6, 7, 1, 2]))  # False
