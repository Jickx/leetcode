def find_miss(arr):
    full_arr = [False for _ in range(len(arr) + 2)]
    for i in range(len(arr)):
        full_arr[arr[i] - 1] = True
    res = []
    print(full_arr)
    for i, v in enumerate(full_arr):
        if v is False:
            res.append(i + 1)
    return res


print(find_miss([5, 4, 1]))
print(find_miss([1, 2, 3, 6]))
print(find_miss([]))
