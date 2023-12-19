def subtract_lists(arr1, arr2):
    arr2_dict = {k: 0 for k in set(arr2)}
    for i in arr2:
        arr2_dict[i] += 1
    for i in arr1:
        arr2_dict[i] -= 1
    return [i for i in arr2_dict if arr2_dict[i] > 0]


arr1 = [7, 2, 5, 3, 5, 3]
arr2 = [7, 2, 5, 4, 6, 5, 5, 5, 3, 5, 3]

print(subtract_lists(arr1, arr2))
