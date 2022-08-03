# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must appear as many times
# as it shows in both arrays and you may return the result in any order.

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000

# - What if the given array is already sorted? How would you optimize your
# algorithm?
# - What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# - What if elements of nums2 are stored on disk, and the memory is limited
# such that you cannot load all elements into the memory at once?


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
