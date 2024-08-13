import random

# Generate 5 random numbers
numbers = [random.randint(1, 100) for i in range(5)]

# Display the random numbers
print("Random numbers:", numbers)

# Find and display the maximum and minimum of the numbers
max_number = max(numbers)
min_number = min(numbers)

print("The max number is:", max_number)
print("The min number is:", min_number)
