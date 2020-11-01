import unittest

from temptracker import TempTracker, InvalidTemperatureError, TempTrackerError


class TestTempTracker(unittest.TestCase):
    """Test critical functionality for `TempTracker`.

    To keep things simple, specific sample test-values can be included below as class variables.
    """
    _sample_nested_list = [2, [68, 70, [[110]]], 98, 109, [5, [101, 102]]]
    _sample_min = 2
    _sample_max = 110

    def test_can_instantiate_with_no_args(self):
        tt = TempTracker()
        self.assertIsInstance(tt, TempTracker)
    
    def test_can_instantiate_with_initial_list(self):
        val = [68]
        tt = TempTracker(val)
        self.assertIsInstance(tt, TempTracker) and self.assertEqual(tt[0], val)

    def test_cannot_instantiate_with_invalid_arg(self):
        invalid_val = "98.44"
        with self.assertRaises(TempTrackerError) as err:
            TempTracker(invalid_val)

    def test_cannot_insert_invalid_temperature(self):
        invalid_val = 98.44
        tt = TempTracker()
        with self.assertRaises(InvalidTemperatureError) as err:
            tt.insert(invalid_val)

    def test_get_max(self):
        tt = TempTracker(self._sample_nested_list)
        self.assertEqual(tt.get_max(), self._sample_max)

    def test_get_min(self):
        tt = TempTracker(self._sample_nested_list)
        self.assertEqual(tt.get_min(), self._sample_min)

    def test_get_mean(self):
        tt = TempTracker(self._sample_nested_list)
        self.assertIsInstance(tt.get_mean(), float)

if __name__ == '__main__':
    unittest.main()
