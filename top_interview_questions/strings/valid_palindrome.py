def is_palindrome(s: str) -> bool:
    s = ''.join(map(lambda x: x.lower(), filter(lambda x: x.isalnum(), s)))
    return s == s[::-1]


s = "A man, a plan, a canal: Panama"

print(is_palindrome(s))
