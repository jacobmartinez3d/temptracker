import unittest

from temptracker import EncoreExtendedList


class TestFlatten(unittest.TestCase):
    """Test functionality of custom methods.
    
    TODO: include testing with generators for both python 2/3
    """
    _test_data = (
        [1, 2, ["a", "b", "c"], 3, [[["foo"], 101], "bar"]],
        [1, 2, "a", "b", "c", 3, "foo", 101, "bar"]
    )

    def test_can_flatten(self):
        given_list, expected_result = self._test_data
        l = EncoreExtendedList(given_list).flatten()
        self.assertEqual(
            EncoreExtendedList(given_list).flatten(),
            expected_result
        )

if __name__ == '__main__':
    unittest.main()
