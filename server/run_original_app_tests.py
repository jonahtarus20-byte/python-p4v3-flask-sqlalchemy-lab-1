#!/usr/bin/env python3

# Run the original app tests manually
import sys
sys.path.append('.')

from testing.app_earthquake_test import TestApp as TestEarthquake
from testing.app_magnitude_test import TestApp as TestMagnitude

def run_test(test_method, test_name):
    try:
        test_instance = TestEarthquake()
        test_method(test_instance)
        print(f"✓ {test_name} passed")
        return True
    except Exception as e:
        print(f"✗ {test_name} failed: {e}")
        return False

def run_magnitude_test(test_method, test_name):
    try:
        test_instance = TestMagnitude()
        test_method(test_instance)
        print(f"✓ {test_name} passed")
        return True
    except Exception as e:
        print(f"✗ {test_name} failed: {e}")
        return False

if __name__ == "__main__":
    print("Running original app tests...")

    all_passed = True

    # Earthquake tests
    all_passed &= run_test(TestEarthquake.test_earthquake_found_route, "test_earthquake_found_route")
    all_passed &= run_test(TestEarthquake.test_earthquake_not_found_route, "test_earthquake_not_found_route")
    all_passed &= run_test(TestEarthquake.test_earthquakes_found_response, "test_earthquakes_found_response")
    all_passed &= run_test(TestEarthquake.test_earthquakes_not_found_response, "test_earthquakes_not_found_response")

    # Magnitude tests
    all_passed &= run_magnitude_test(TestMagnitude.test_earthquake_magnitude_route, "test_earthquake_magnitude_route")
    all_passed &= run_magnitude_test(TestMagnitude.test_earthquakes_magnitude_match_response, "test_earthquakes_magnitude_match_response")
    all_passed &= run_magnitude_test(TestMagnitude.test_earthquakes_magnitude_no_match_response, "test_earthquakes_magnitude_no_match_response")

    if all_passed:
        print("\nAll original app tests passed!")
    else:
        print("\nSome tests failed!")
