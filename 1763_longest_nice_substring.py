from collections import defaultdict


def longest_nice_substring(s):
    left = 0
    right = 1
    max_len = 1
    result = ''
    while right < len(s):
        if s[left].lower() != s[right].lower():
            left += 1
            right += 1
        else:
            chars = s[left]
            while (right < len(s)) and (s[left].lower() == s[right].lower()):
                chars += s[right]
                right += 1

            if len(set(list(chars))) != len(set([i.lower() for i in chars])):
                if len(chars) > max_len:
                    result = chars
                max_len = len(chars)
            left = right
            right += 1
    return result


print(longest_nice_substring('YazaAayYy'))  # aAa
print(longest_nice_substring('Bb'))  # Bb
print(longest_nice_substring('c'))  # ''
print(longest_nice_substring('cChH'))  # 'cChH'
print(longest_nice_substring('dDzeE'))  # 'dD'
