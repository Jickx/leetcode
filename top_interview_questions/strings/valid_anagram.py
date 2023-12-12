def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
# true

# s = "rat"
# t = "car"
# false

print(is_anagram(s, t))