#Function 1
def is_even_or_odd(number):
    """Determines if a number is even or odd"""
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"
#Function 2
def temperature_converter(temp, from_unit):
    """Converts temperature between Celsius and Fahrenheit"""
    if from_unit.lower() == "celsius":
        fahrenheit = (temp * 9/5) + 32
        return f"{temp}°C = {fahrenheit}°F"
    elif from_unit.lower() == "fahrenheit":
        celsius = (temp - 32) * 5/9
        return f"{temp}°F = {celsius:.1f}°C"
    else:
        return "Invalid unit. Use 'celsius' or 'fahrenheit'"
