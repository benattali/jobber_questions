import unittest


def nextVersion(version_num: str) -> str:
    # iterate through the string in reverse order
    ## if char is a period
    ### add it to temp_str
    ## if loop reaches the last element (i.e the first number)
    ### increment that digit by 1 and add it to new_version
    ## if char is 9
    ### add 0 to temp_str
    ## if char is not 9
    ### increment that digit by 1 and add it to new_version and break from the loop

    temp_str = ""
    new_version = ""

    for i, char in enumerate(reversed(version_num)):
        if char == ".":
            temp_str += char
        elif i == len(version_num) - 1:
            temp_num = int(char) + 1
            new_version += version_num[: -1 - i] + str(temp_num) + temp_str[::-1]
        elif int(char) == 9:
            temp_str += "0"
        else:
            temp_num = int(char) + 1
            new_version += version_num[: -1 - i] + str(temp_num) + temp_str[::-1]
            break

    return new_version


# Tests


class Test(unittest.TestCase):
    def test_one_number(self):
        actual = nextVersion("1")
        expected = "2"
        self.assertEqual(actual, expected)

    def test_multiple_numbers(self):
        actual = nextVersion("1.2.3")
        expected = "1.2.4"
        self.assertEqual(actual, expected)

    def test_version_ends_with_nine(self):
        actual = nextVersion("9.9")
        expected = "10.0"
        self.assertEqual(actual, expected)

    def test_version_ends_with_nine_no_decimal(self):
        actual = nextVersion("99")
        expected = "100"
        self.assertEqual(actual, expected)

    def test_version_starts_with_9_digit_ends_with_0(self):
        actual = nextVersion("99.0")
        expected = "99.1"
        self.assertEqual(actual, expected)

    def test_version_starts_with_9_digit_ends_with_9(self):
        actual = nextVersion("99.0.9")
        expected = "99.1.0"
        self.assertEqual(actual, expected)

    def test_version_starts_with_9_digit_ends_with_two_0s(self):
        actual = nextVersion("99.0.0")
        expected = "99.0.1"
        self.assertEqual(actual, expected)

    def test_version_ends_with_multiple_nines(self):
        actual = nextVersion("0.9.9")
        expected = "1.0.0"
        self.assertEqual(actual, expected)

    def test_version_has_multiple_numbers_starts_with_0_ends_with_nine(self):
        actual = nextVersion("0.8.9")
        expected = "0.9.0"
        self.assertEqual(actual, expected)

    def test_version_has_multiple_numbers_starts_with_0(self):
        actual = nextVersion("0.8.1")
        expected = "0.8.2"
        self.assertEqual(actual, expected)

    def test_version_large_number(self):
        actual = nextVersion("10001")
        expected = "10002"
        self.assertEqual(actual, expected)

    def test_version_large_number_ends_with_9(self):
        actual = nextVersion("10009")
        expected = "10010"
        self.assertEqual(actual, expected)

    def test_version_large_number_ends_with_9_decimal_ends_with_9(self):
        actual = nextVersion("10009.9")
        expected = "10010.0"
        self.assertEqual(actual, expected)

    def test_version_chain_the_9s(self):
        actual = nextVersion("9.9.9.9.9.9.9.9.9.9.9.9.9")
        expected = "10.0.0.0.0.0.0.0.0.0.0.0.0"
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
