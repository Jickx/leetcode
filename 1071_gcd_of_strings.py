from math import gcd


def gcd_of_strings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ''
    gcd_length = gcd(len(str1), len(str2))
    return str1[:gcd_length]


print(gcd_of_strings("ABCABC", "ABC"))  # 'ABC'
print(gcd_of_strings("ABABAB", "ABAB"))  # 'AB'
