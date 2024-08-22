def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # String containing all vowels (both lowercase and uppercase)
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Input string
input_string = "Welcome to Python Assignment"

# Count the vowels
total_vowels = count_vowels(input_string)

# Output the result
print(f"Total vowels are: {total_vowels}")
