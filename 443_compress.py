def compress(chars):
    result = 0
    i = 0
    while i < len(chars):
        letter = chars[i]
        ctr = 0
        while i < len(chars) and chars[i] == letter:
            ctr += 1
            i += 1
        chars[result] = letter
        result += 1
        if ctr > 1:
            for c in str(ctr):
                chars[result] = str(c)
                result += 1
    for _ in range(len(chars) - result):
        chars.pop()

    return chars


print(compress(["a", "a", "b", "b", "c", "c", "c", "c", "c", "c", "c", "c"]))  # 6
