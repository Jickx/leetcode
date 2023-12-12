# You are given an n x n 2D matrix representing an image, rotate the image
# by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

from icecream import ic


def rotate_image(matrix):
    size = len(matrix)

    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for line in matrix:
        left = 0
        right = size - 1
        while left <= right:
            temp = line[left]
            line[left] = line[right]
            line[right] = temp
            left += 1
            right -= 1


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotate_image(matrix)

for line in matrix:
    ic(line)
