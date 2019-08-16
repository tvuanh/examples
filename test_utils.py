import unittest

import utils


class TestSelectColumns(unittest.TestCase):

    def test_select_columns(self):
        columns = ["a", "b", "c", "d", "e"]

        expected = [1]
        actual = utils.select_columns(columns, labels=["b"])
        self.assertListEqual(actual, expected)

        expected = [1, 4]
        actual = utils.select_columns(columns, labels=["b", "e"])
        self.assertListEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
