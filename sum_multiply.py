# Function to calculate the multiplication of two numbers
def calculateMultiplication(num1, num2):
    # Multiply num1 and num2 and store the result in multiplicationResult
    multiplicationResult = num1 * num2
    return multiplicationResult

# Function to calculate the sum of two numbers
def calculateSum(num1, num2):
    # Add num1 and num2 and store the result in sumResult
    sumResult = num1 + num2
    return sumResult

# Main part of the program
if __name__ == "__main__":
    # Define two numbers to use in calculations
    number1 = 5
    number2 = 10

    # Call the calculateMultiplication function and store the result
    resultMultiplication = calculateMultiplication(number1, number2)
    # Call the calculateSum function and store the result
    resultSum = calculateSum(number1, number2)

    # Print the results to the console
    print(f"The multiplication of {number1} and {number2} is: {resultMultiplication}")
    print(f"The sum of {number1} and {number2} is: {resultSum}")
