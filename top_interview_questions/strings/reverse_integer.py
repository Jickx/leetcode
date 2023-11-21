from icecream import ic


def reverse_integer(num):
    rev_num = int(str(num)[::-1].strip('-'))

    if rev_num > 2 ** 32:
        return 0

    if num > 0:
        return rev_num
    return -rev_num


assert reverse_integer(-123) == -321
assert reverse_integer(123) == 321
assert reverse_integer(-3200) == -23
assert reverse_integer(-2 ** 34) == 0
assert reverse_integer(0) == 0
assert reverse_integer(1534236469) == 0
