import unittest
from system_check import reactor_status

class TestReactor(unittest.TestCase):

    def test_negative_checks(self):
        self.assertEqual((15, -5), "Sensor Error")

    def test_critical(self):
        self.assertEqual((2100, 459), "CRITICAL")

    def test_warning(self):
        self.assertEqual((1500, 115), "WARNING")

    def test_maintenance(self):
        self.assertEqual((475, 56), "Maintenance Mode")

    def test_normal_operation(self):
        self.assertEqual((250, 35), "Normal Operation")

if __name__ == "__main__":
    unittest.main()