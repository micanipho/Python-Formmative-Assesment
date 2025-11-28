import unittest
from system_check import reactor_status

class testReactor(unittest.TestCase):
    def test_reactor(self):
        self.assertEqual(reactor_status(-1, 5), "Sensor Error")
        self.assertEqual(reactor_status(3000, 600), "CRITICAL")
        self.assertEqual(reactor_status(1400, 150), "WARNING")
        self.assertEqual(reactor_status(400, 80), "Maintenance Mode")
        self.assertEqual(reactor_status(700, 80), "Normal Operation")

if __name__ == "__main__":
    unittest.main()