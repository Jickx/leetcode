# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
from collections import defaultdict


# O(n2)

# def first_uniq_char(s: str) -> int:
#     i = 0
#     while i < len(s):
#         if s[i] not in s[:i] + s[i + 1:]:
#             return i
#         i += 1
#     return -1

def first_uniq_char(s: str) -> int:
    s_dict = defaultdict(lambda: 0)
    for i in s:
        s_dict[i] += 1
    for k, v in s_dict.items():
        if v == 1:
            return s.index(k)
    return -1


input = ["leetcode", "loveleetcode", "aabb"]
for s in input:
    print(first_uniq_char(s))
