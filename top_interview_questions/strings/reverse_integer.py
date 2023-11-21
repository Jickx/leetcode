from icecream import ic


def reverse_integer(num):
    if num == 0:
        return 0

    if num != abs(num):
        pos = False
    else:
        pos = True

    num_str = str(num).lstrip('-').lstrip('0')
    rev_num_str = int(num_str[::-1])

    if rev_num_str >= 2 ** 31 - 1 or rev_num_str <= -2 ** 31:
        return 0

    if pos:
        return rev_num_str
    return -rev_num_str


assert reverse_integer(-123) == -321
assert reverse_integer(123) == 321
assert reverse_integer(-3200) == -23
assert reverse_integer(-2 ** 34) == 0
assert reverse_integer(0) == 0
assert reverse_integer(1534236469) == 0
