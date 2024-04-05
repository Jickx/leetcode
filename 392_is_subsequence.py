def is_subsequence(s, t):
    sp = tp = 0
    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
        tp += 1
    return sp == len(s)

print(is_subsequence("abc", "ahbgdc"))  # True
print(is_subsequence("axc", "ahbgdc"))  # False
print(is_subsequence("b", "c"))  # False
print(is_subsequence("b", "abc"))  # True
print(is_subsequence("aaaaaa", "bbaaaa"))  # False
