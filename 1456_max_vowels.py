def max_vowels(s, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    max_vow = vow = sum(s[:k].count(vowel) for vowel in vowels)
    l = 1
    r = k
    while r < len(s):
        if s[l - 1] in vowels:
            vow -= 1
        if s[r] in vowels:
            vow += 1
        if vow > max_vow:
            max_vow = vow
        l += 1
        r += 1
    return max_vow


print(max_vowels("abciiidef", 3))  # 3
print(max_vowels("aeiou", 2))  # 2
print(max_vowels("leetcode", 3))  # 2
print(max_vowels("novowels", 1))  # 1
print(max_vowels("tnfazcwrryitgacaabwm", 4))  # 3
