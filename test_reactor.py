import unittest
from system_check import reactor_status

class TestReactor:

    def test_critical(self):
        self.assertEqual(reactor_status(2500, 10), "CRITICAL")
        self.assertEqual(reactor_status(500, 600), "CRITICAL")


    def test_warning(self):
        self.assertEqual(reactor_status(1500, 200), "WARNING")
        self.assertEqual(reactor_status(1000, 200), "WARNING")

    def test_normal(self):
        self.assertEqual(reactor_status(800, 50), "Normal Operation")

if __name__ == '__main__':
    unittest.main()