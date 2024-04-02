def can_place_flowers(flowerbed: list[int], n: int) -> bool:
    for i in range(len(flowerbed)):
        if (i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0) or (
                i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0):
            flowerbed[i] = 1
            n -= 1
        elif flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1
    print(n)
    return True if n <= 0 else False


print(can_place_flowers([1, 0, 0, 0, 1], 2))  # False
print(can_place_flowers([0, 0, 1, 0, 1], 1))  # True
print(can_place_flowers([1, 0, 1, 0, 0], 1))  # True
