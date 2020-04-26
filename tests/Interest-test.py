import unittest
from finfun import Interest as i


class MyTestCase(unittest.TestCase):
    def test_something(self):
        end_value = i.compound(1000, 5, 1)
        self.assertEqual(end_value, 1050)
        self.assertEqual(i.compound(1000, 0.05, 1), end_value)


if __name__ == '__main__':
    unittest.main()
