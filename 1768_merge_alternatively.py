def merge(word1, word2):
    if max(len(word1), len(word2)) == len(word1):
        max_word, min_word = word1, word2
    else:
        max_word, min_word = word2, word1
    result = ''
    ln = 0
    for i in range(len(min_word)):
        result += word1[i] + word2[i]
        ln = i

    return result + max_word[ln + 1:]


print(merge(word1="abc", word2="pqr"))  # a p b q c r
print(merge(word1="ab", word2="pqrs"))  # a p b q   r   s
