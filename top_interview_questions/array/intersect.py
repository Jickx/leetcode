# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must appear as many times
# as it shows in both arrays and you may return the result in any order.

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    result = []
    while nums1:
        el1 = nums1.pop()
        for i, el2 in enumerate(nums2):
            if el1 == el2:
                nums2[i] = None
                result.append(el1)
                break
    return result


assert intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
assert intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9] or [9, 4]
