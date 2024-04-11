def decrypt(code, k):
    result = []
    if k == 0:
        return [0] * len(code)

    for i in range(len(code)):
        n = 0
        for j in range(abs(k)):
            if k > 0:
                n += code[(len(code) + j + i + 1) % len(code)]
            elif k < 0:
                n += code[i - (len(code) + j + 1) % len(code)]
        result.append(n)
    return result


# print(decrypt([5, 7, 1, 4], 3))  # [12, 10, 16, 13]
print(decrypt([2, 4, 9, 3], -2))  # [12, 5, 6, 13]
print(decrypt([5, 7, 1, 4], 0))  # [0, 0, 0, 0]
