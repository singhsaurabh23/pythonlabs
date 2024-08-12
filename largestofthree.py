#taking input from the user
num1=float(input("Enter the first number:"))
num2=float(input("Enter the second number:"))
num3=float(input("Enter the third number:"))
#checking condition of largest number
if num1 >= num2 and num1 >= num3:
        print( num1)

        
elif num2 >= num1 and num2 >= num3:
        print(num2)
else:
        print(num3)
