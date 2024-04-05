def max_area(height):
    start = 0
    end = len(height) - 1
    max_area = 0

    while start < end:
        length = min(height[start], height[end])
        width = end - start
        area = length * width

        if area > max_area:
            max_area = area

        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
    return max_area


print(max_area([5, 8, 6, 2, 5, 4, 8, 3, 7]))
