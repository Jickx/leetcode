def contains_duplicates(nums: list[int]) -> bool:
    while nums:
        if nums.pop() in nums:
            return True
    return False


assert contains_duplicates([1, 2, 3, 4, 1]) == True
assert contains_duplicates([1, 2, 3, 4]) == False
assert contains_duplicates([1, 1, 1, 2, 3, 4]) == True


