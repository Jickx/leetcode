from collections import defaultdict


def maximum_length_substring(s):
    left = 0
    right = 1
    max_len = 0
    chars_count = defaultdict(int)
    chars_count[s[0]] = 1
    while right < len(s):
        chars_count[s[right]] += 1
        if chars_count[s[right]] > 2:
            max_len = max(len(s[left:right]), max_len)
            while chars_count[s[right]] > 2:
                chars_count[s[left]] -= 1
                left += 1
        right += 1
    return max(len(s[left:right]), max_len)


print(maximum_length_substring('bcbbbcba'))  # 4
print(maximum_length_substring('aaaa'))  # 2
print(maximum_length_substring('acedc'))  # 5
print(maximum_length_substring('ccdcb'))  # 4
