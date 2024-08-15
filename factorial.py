number=int(input("Enter the number for which you want to find the factorial:"))

#initialising the varialble for factorial
factorial=1

#storing original number for reference
original_number=number

while number>0:
    factorial*=number#multiply the current number
    number-=1# decreasing the number by 1

#priniting the output
print("The factorial of number is :",factorial)
