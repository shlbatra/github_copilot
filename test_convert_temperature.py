# Provided Comment:
# Test Requirements:
# - Import necessary libraries
# - Write a test function named `test_convert_temperature`
# - Test the following scenarios:
#   1. Celsius to Fahrenheit conversion
#   2. Celsius to Kelvin conversion
#   3. Fahrenheit to Celsius conversion
#   4. Fahrenheit to Kelvin conversion
#   5. Kelvin to Celsius conversion
#   6. Kelvin to Fahrenheit conversion
#   7. Invalid input units
#   8. Invalid output units
# - Use assert statements to compare the expected and actual results
# - Account for floating-point rounding errors 
#   by using a small delta for comparison

# Generated Code

import pytest

from convert_temperature import convert_temperature

def test_convert_temperature():
    # Celsius to Fahrenheit conversion
    assert abs(convert_temperature(0, "C", "F") - 32) < 0.0001
    assert abs(convert_temperature(100, "C", "F") - 212) < 0.0001
    assert abs(convert_temperature(-40, "C", "F") + 40) < 0.0001

    # Celsius to Kelvin conversion
    assert abs(convert_temperature(0, "C", "K") - 273.15) < 0.0001
    assert abs(convert_temperature(100, "C", "K") - 373.15) < 0.0001
    assert abs(convert_temperature(-273.15, "C", "K")) < 0.0001

    # Fahrenheit to Celsius conversion
    assert abs(convert_temperature(32, "F", "C")) < 0.0001
    assert abs(convert_temperature(212, "F", "C") - 100) < 0.0001
    assert abs(convert_temperature(-40, "F", "C") + 40) < 0.0001

    # Fahrenheit to Kelvin conversion
    assert abs(convert_temperature(32, "F", "K") - 273.15) < 0.0001
    assert abs(convert_temperature(212, "F", "K") - 373.15) < 0.0001
    assert abs(convert_temperature(-40, "F", "K") + 233.15) < 0.0001

    # Kelvin to Celsius conversion
    assert abs(convert_temperature(0, "K", "C")) < 0.0001
    assert abs(convert_temperature(273.15, "K", "C") - 0) < 0.0001
    assert abs(convert_temperature(373.15, "K", "C") - 100) < 0.0001

    # Kelvin to Fahrenheit conversion
    assert abs(convert_temperature(0, "K", "F") + 32) < 0.0001
    assert abs(convert_temperature(273.15, "K", "F") - 32) < 0.0001
    assert abs(convert_temperature(373.15, "K", "F") - 212) < 0.0001