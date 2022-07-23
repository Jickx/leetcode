def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    result = []
    for i in nums1:
        if i in nums2:
            result.append(i)
    return result


assert intersect([2, 2, 1, 1], [2, 2]) == [2, 2]
assert intersect([1, 2, 3, 4], [2, 3, 5]) == [2, 3]