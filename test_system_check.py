import unittest
import os
from system_check import (
    get_departure_airport,
    check_baggage_allowance,
    validate_flight_number,
    is_leap_year,
    reactor_status
)

class TestSystemCheck(unittest.TestCase):

    def test_00_tdd_file_exists(self):
        print("\nGrading Pre-Check: Looking for student test file...")
        file_exists = os.path.exists("test_reactor.py")
        
        self.assertTrue(
            file_exists, 
            msg="❌ FAILED: 'test_reactor.py' was not found. Did you create the file?"
        )
        print("✅ FOUND: 'test_reactor.py' exists.")

    def test_q1_departure_airport(self):
        print("Grading Q1: Departure Airport...")
        self.assertEqual(get_departure_airport("FL-JO234-JNB-CPT-2023"), "JNB")
        self.assertEqual(get_departure_airport("BS-XY99999-LHR-JFK-2024"), "LHR")
        self.assertEqual(get_departure_airport("EC-A1-DBN-JNB-2023"), "DBN")

    def test_q2_baggage_allowance(self):
        print("Grading Q2: Baggage Allowance...")
        self.assertEqual(check_baggage_allowance("EC-JO234-JNB-CPT"), "Economy - 20kg")
        self.assertEqual(check_baggage_allowance("BS-JO234-JNB-CPT"), "Business - 40kg")
        self.assertEqual(check_baggage_allowance("FL-JO234-JNB-CPT"), "First Class - 60kg")
        self.assertEqual(check_baggage_allowance("XX-JO234-JNB-CPT"), "Standard - 0kg")

    def test_q3_validate_flight_number(self):
        print("Grading Q3: Flight Number Parsing...")
        self.assertEqual(validate_flight_number("FL-JO234-JNB-CPT"), "Valid - Northbound")
        self.assertEqual(validate_flight_number("FL-JO235-JNB-CPT"), "Valid - Southbound")
        self.assertEqual(validate_flight_number("FL-A9-JNB-CPT"), "Valid - Southbound")
        self.assertEqual(validate_flight_number("FL-JOABC-JNB-CPT"), "Invalid Flight")

    def test_q4_leap_year(self):
        print("Grading Q4: Leap Year Logic...")
        self.assertTrue(is_leap_year(2024))
        self.assertFalse(is_leap_year(2023))
        self.assertTrue(is_leap_year(1900))
        self.assertTrue(is_leap_year(2000))

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
