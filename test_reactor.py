import unittest
from system_check import reactor_status



class TestReactor (unittest.TestCase):
    def test_normal_sensors(self):
        self.assertEqual(reactor_status(501,80), "Normal operation")

    def test_invalid_sensors(self):
        self.assertEqual(reactor_status(-1, -5), "Sensor Error")
        self.assertEqual(reactor_status(-10, 2), "Sensor Error")
        self.assertEqual(reactor_status(1,-5), "Sensor Error")

    def test_critical_sensors(self):
        self.assertEqual(reactor_status(2000, 502), "CRITICAL")
        self.assertEqual(reactor_status(2500, 501), "CRITICAL")
        self.assertEqual(reactor_status(2001,504), "CRITICAL")

    def test_unstable_sensors(self):
        self.assertEqual(reactor_status(1500, 200), "WARNING")
        self.assertEqual(reactor_status(2000, 500), "WARNING")
        self.assertEqual(reactor_status(1000,150), "WARNING")

    def test_maintenance_mode(self):
        self.assertEqual(reactor_status(400, 100), "Maintenance Mode")
        self.assertEqual(reactor_status(490, 70), "Maintenance Mode")
        self.assertEqual(reactor_status(100, 50), "Maintenance Mode")



if __name__ == '__main__':
    unittest.main()
    
    