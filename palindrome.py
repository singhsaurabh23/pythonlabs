#input to check a number is a palindrome or not
number=int(input("Enter the number you want to check:"))

#store the original number
original_number=number

#intialise the variable to store the reversed number
reversed_number=0
#conditon to reverse the number
while number>0:
    digit=number%10
    reversed_number=reversed_number*10+digit
    number=number//10
#to check whether reversed number is equal to the original number
if original_number==reversed_number:
    print("Entered number is a palindrome")

else:
    print("Entered number is not a palindrome")
