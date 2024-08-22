def count_characters(input_string):
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    special_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1  # Count uppercase letters
        elif char.islower():
            lowercase_count += 1  # Count lowercase letters
        elif char.isdigit():
            number_count += 1  # Count numeric digits
        else:
            special_count += 1  # Count special characters

    return uppercase_count, lowercase_count, number_count, special_count

# Input string
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Count the characters
uppercase_count, lowercase_count, number_count, special_count = count_characters(input_string)

# Output the result
print(f"UpperCase : {uppercase_count}")
print(f"LowerCase : {lowercase_count}")
print(f"NumberCase : {number_count}")
print(f"SpecialCase : {special_count}")
