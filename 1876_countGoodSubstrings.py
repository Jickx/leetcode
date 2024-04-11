def count_good_substrings(s):
    result = 0
    left = 0
    right = 3
    while right <= len(s):
        if len(s[left:right]) == len(set(s[left:right])):
            result += 1
        left += 1
        right += 1
    return result


print(count_good_substrings('xyzzaz'))  # 1
print(count_good_substrings('aababcabc'))  # 4
