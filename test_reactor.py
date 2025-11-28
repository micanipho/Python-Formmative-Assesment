import unittest
import os
from system_check import reactor_status

class TestReactor(unittest.TestCase):

    def test_00_tdd_file_exists(self):
        print("\nGrading Pre-Check: Looking for student test file...")
        file_exists = os.path.exists("test_reactor.py")
        
        self.assertTrue(
            file_exists, 
            msg="❌ FAILED: 'test_reactor.py' was not found. Did you create the file?"
        )
        print("✅ FOUND: 'test_reactor.py' exists.")

    def test_q5_reactor_status(self):
        print("Grading Q5: Reactor Logic...")
        self.assertEqual(reactor_status(-1, 50), "Sensor Error")
        self.assertEqual(reactor_status(500, -10), "Sensor Error")
        self.assertEqual(reactor_status(2500, 10), "CRITICAL")
        self.assertEqual(reactor_status(500, 600), "CRITICAL")
        self.assertEqual(reactor_status(1500, 200), "WARNING")
        self.assertEqual(reactor_status(1000, 200), "WARNING")
        self.assertEqual(reactor_status(400, 50), "Maintenance Mode")
        self.assertEqual(reactor_status(800, 50), "Normal Operation")

if __name__ == '__main__':
    unittest.main(failfast=True, verbosity=0)