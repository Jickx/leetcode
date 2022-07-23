def contains_duplicates(nums: list[int]) -> bool:
    return False if len(set(nums)) == len(nums) else True


assert contains_duplicates([1, 2, 3, 4, 1]) == True
assert contains_duplicates([1, 2, 3, 4]) == False
assert contains_duplicates([1, 1, 1, 2, 3, 4]) == True


