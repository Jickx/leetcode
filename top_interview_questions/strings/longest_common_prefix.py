def longest_common_prefix(strs: list[str]) -> str:
    strs.sort()
    first_str = strs[0]
    last_str = strs[-1]

    result = ''

    for i in range(len(first_str)):
        if last_str[i] == first_str[i]:
            result += last_str[i]
        else:
            break
    return result


assert longest_common_prefix(["flower", "flow", "flight"]) == 'fl'
assert longest_common_prefix(["dog", "racecar", "car"]) == ''
