def convert_temperature(temperature, unit):              
    """
    Converts a temperature value to Celsius, Fahrenheit, and Kelvin.

    Args:
        temperature (float): The temperature value.
        unit (str): The original unit of measurement ('C', 'F', or 'K').

    Returns:
        tuple: A tuple containing the converted temperatures in Celsius, Fahrenheit, and Kelvin.
    """

    if unit.upper() == 'C':
        celsius = temperature
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
    elif unit.upper() == 'F':
        fahrenheit = temperature
        celsius = (fahrenheit - 32) * 5/9
        kelvin = celsius + 273.15
    elif unit.upper() == 'K':
        kelvin = temperature
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9/5) + 32
    else:
        raise ValueError("Invalid unit of measurement. Please use 'C', 'F', or 'K'.")

    return celsius, fahrenheit, kelvin

def main():
    """
    Prompts the user for temperature and unit, then converts and displays the results.
    """

    while True:
        try:
            temperature = float(input("Enter the temperature value: "))
            unit = input("Enter the original unit of measurement (C, F, or K): ")
            celsius, fahrenheit, kelvin = convert_temperature(temperature, unit)

            print(f"Converted temperatures:")
            print(f"Celsius: {celsius:.2f} °C")
            print(f"Fahrenheit: {fahrenheit:.2f} °F")
            print(f"Kelvin: {kelvin:.2f} K")

            break  # Exit the loop on successful conversion
        except ValueError:
            print("Invalid input. Please enter a valid number and unit.")

if __name__ == "__main__":
    main()