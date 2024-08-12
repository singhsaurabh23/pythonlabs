# Function to convert Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    # Formula to convert Celsius to Fahrenheit: (Celsius * 9/5) + 32
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Main part of the program
if __name__ == "__main__":
    # Define a temperature in Celsius
    celsiusTemperature = 37


    # Call the conversion function and store the result
    fahrenheitTemperature = celsiusToFahrenheit(celsiusTemperature)

    # Print the result
    print(f"{celsiusTemperature} degrees Celsius is equal to {fahrenheitTemperature} degrees Fahrenheit.")
