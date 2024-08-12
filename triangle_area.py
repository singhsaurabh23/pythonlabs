import math

# Function to calculate the area of a triangle using Heron's formula
def calculateTriangleArea(side1, side2, side3):
    # Calculate the semi-perimeter of the triangle
    semiPerimeter = (side1 + side2 + side3) / 2

    # Calculate the area using Heron's formula
    area = math.sqrt(semiPerimeter * (semiPerimeter - side1) * (semiPerimeter - side2) * (semiPerimeter - side3))
    return area

# Main part of the program
if __name__ == "__main__":
    # Define the sides of the triangle
    side1 = 3
    side2 = 4
    side3 = 5

    # Call the function to calculate the area
    triangleArea = calculateTriangleArea(side1, side2, side3)

    # Print the result
    print(f"The area of the triangle with sides {side1}, {side2}, and {side3} is: {triangleArea:.2f}")
