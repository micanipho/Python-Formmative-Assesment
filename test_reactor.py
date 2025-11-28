import unittest
from system_check import reactor_status

class TestReactor(unittest.TestCase):
    def testreactor(self):
        self.assertEqual(reactor_status(-1, 50), "Sensor Error")
        self.assertEqual(reactor_status(500, -10), "Sensor Error")
        self.assertEqual(reactor_status(2500, 10), "CRITICAL")
        self.assertEqual(reactor_status(500, 600), "CRITICAL")
        self.assertEqual(reactor_status(1500, 200), "WARNING")
        self.assertEqual(reactor_status(1000, 200), "WARNING")
        self.assertEqual(reactor_status(400, 50), "Maintenance Mode")
        self.assertEqual(reactor_status(800, 50), "Normal Operation")

if __name__ == '__main__':
    unittest.main()