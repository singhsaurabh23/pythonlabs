#input string
input_string="P@#yn26at^&i5ve"

#initialize counters for characters,symbols and digit count
char_count=0
digit_count=0
symbol_count=0

#condition to check number of occurences
for char in input_string:
    if char.isalpha():
        char_count+=1
    elif char.isdigit():
        digit_count+=1
    else:
        symbol_count+=1
#print count of each values
print(f"chars={char_count}")
print(f"digit={digit_count}")
print(f"symbol={symbol_count}")
