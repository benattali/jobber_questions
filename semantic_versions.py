import unittest


def nextVersion(version_num: str) -> str:
    if len(version_num) < 1:
        raise ValueError("An empty string was passed.")

    temp_str = ""
    new_version = ""
    for i, char in enumerate(reversed(version_num)):
        if char == ".":
            temp_str += char
        elif i == len(version_num) - 1:
            temp = int(char) + 1
            new_version += version_num[: -1 - i] + str(temp) + temp_str[::-1]
        elif int(char) == 9:
            temp_str += "0"
        else:
            temp = int(char) + 1
            new_version += version_num[: -1 - i] + str(temp) + temp_str[::-1]
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

    def test_version_ends_with_nine(self):
        actual = nextVersion("99")
        expected = "100"
        self.assertEqual(actual, expected)

    def test_version_ends_with_multiple_nines(self):
        actual = nextVersion("0.9.9")
        expected = "1.0.0"
        self.assertEqual(actual, expected)

    def test_error_with_empty_string(self):
        with self.assertRaises(ValueError):
            nextVersion("")


unittest.main(verbosity=2)
