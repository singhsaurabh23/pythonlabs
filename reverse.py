#getting input from the user
number=int(input("Enter the number that you want to reverse:"))
#initializing the variable to store reverse number
reversed_Number=0

while number>0:
    #to get the last digit of the number
    digit=number%10

    reversed_Number=reversed_Number*10 + digit
    
#to remove the last digit of the original number
    number=number//10

print("Reversed number:",reversed_Number)
