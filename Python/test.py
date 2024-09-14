from calculate import Calculate
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculate = Calculate()
    def test_add(self):
        self.assertEqual(self.calculate.plus(4), 8)