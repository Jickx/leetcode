def reverse_words(s: str) -> str:
    s_lst = s.split()
    s_lst.reverse()
    return ' '.join([i for i in s_lst])


print(reverse_words("the sky is blue"))
