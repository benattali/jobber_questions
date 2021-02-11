import unittest


def get_next_location(row: int, column: int, dir: str) -> list[int]:
    # find the row and column that need to be looked at next

    if dir == "l_to_r":
        column += 1
    elif dir == "t_to_b":
        row += 1
    elif dir == "r_to_l":
        column -= 1
    elif dir == "b_to_t":
        row -= 1

    return [row, column]


def createSpiral(n: int) -> list[list[int]]:
    # initialize 2d list (spiral), dir, row and column vars
    # loop n**2 times
    ## start with going from left to right
    ## assign spiral at [row][column] to the loop iterator + 1
    ## find the next row and column to assign a value to
    ## if row or column reach n, or if spiral at [row][column] has already been assigned
    ### change dir
    ### if dir changed from b_to_t to something else
    #### change dir to start from l_to_r again

    if n < 1:
        return []

    spiral = [[0] * n for _ in range(n)]
    row = 0
    column = 0
    dir = ["l_to_r", "t_to_b", "r_to_l", "b_to_t"]
    dir_counter = 0

    for i in range(n ** 2):
        spiral[row][column] = i + 1
        temp_row, temp_column = get_next_location(row, column, dir[dir_counter])
        if temp_row >= n or temp_column >= n or spiral[temp_row][temp_column] != 0:
            dir_counter += 1
            if dir_counter >= len(dir):
                dir_counter = 0
            temp_row, temp_column = get_next_location(row, column, dir[dir_counter])
        row = temp_row
        column = temp_column

    return spiral


# Tests


class Test(unittest.TestCase):
    def test_spiral_n_is_0(self):
        actual = createSpiral(0)
        expected = []
        self.assertEqual(actual, expected)

    def test_spiral_n_is_1(self):
        actual = createSpiral(1)
        expected = [[1]]
        self.assertEqual(actual, expected)

    def test_spiral_n_is_2(self):
        actual = createSpiral(2)
        expected = [[1, 2], [4, 3]]
        self.assertEqual(actual, expected)

    def test_spiral_small_number(self):
        actual = createSpiral(3)
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(actual, expected)

    def test_spiral_large_number(self):
        actual = createSpiral(9)
        expected = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [32, 33, 34, 35, 36, 37, 38, 39, 10],
            [31, 56, 57, 58, 59, 60, 61, 40, 11],
            [30, 55, 72, 73, 74, 75, 62, 41, 12],
            [29, 54, 71, 80, 81, 76, 63, 42, 13],
            [28, 53, 70, 79, 78, 77, 64, 43, 14],
            [27, 52, 69, 68, 67, 66, 65, 44, 15],
            [26, 51, 50, 49, 48, 47, 46, 45, 16],
            [25, 24, 23, 22, 21, 20, 19, 18, 17],
        ]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
