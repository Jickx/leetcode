# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

import re


# def my_atoi(s: str) -> int:
#     s = s.strip(' ')
#     if s == '' or s == '+' or s == '-':
#         return 0
#     result = []
#     i = 0
#     pos = None
#     while i < len(s):
#         if s[i] == '-' and pos is None and not result:
#             i += 1
#             pos = False
#             continue
#         elif s[i] == '+' and pos is None and not result:
#             i += 1
#             pos = True
#             continue
#         elif (s[i] == '+' or s[i] == '-') and pos is not None and not result:
#             return 0
#         if not s[i].isnumeric() and not result:
#             return 0
#         elif not s[i].isnumeric() and result:
#             break
#         elif s[i].isnumeric():
#             result.append(s[i])
#             if pos is None:
#                 pos = True
#             i += 1
#     result = int(''.join(result)) if pos else -int(''.join(result))
#     if result > 2 ** 31 - 1:
#         return 2147483647
#     elif result < -2 ** 31:
#         return -2147483648
#     return result


def my_atoi(s: str) -> int:
    match = re.match(r'^([+-]?)([0-9]+)', s.strip())
    if not match:
        return 0
    sign, value = match.groups()
    if sign == '-':
        result = -int(value)
    else:
        result = int(value)
    if result > 2 ** 31 - 1:
        return 2147483647
    elif result < -2 ** 31:
        return -2147483648
    return result


assert my_atoi('') == 0
assert my_atoi(' ') == 0
assert my_atoi('+') == 0
assert my_atoi('  ') == 0
assert my_atoi('+3-') == 3
assert my_atoi('-+42') == 0
assert my_atoi('-42') == -42
assert my_atoi('-13+8') == -13
assert my_atoi('    +42') == 42
assert my_atoi('    -42') == -42
assert my_atoi('words and 987') == 0
assert my_atoi('4193 with words') == 4193
assert my_atoi('2147483648') == 2147483647
assert my_atoi('-2147483649 words and ') == -2147483648
