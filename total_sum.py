#initialising total sum
total_sum=0

#using while the condition is True
while True:
    number=int(input("Enter a number (enter 0 to stop):"))
#to exit the loop after user gives 0 as input
    if number ==0:
        break
#adding all the numbers entered by the user
    total_sum+=number
#printing the output
print("Total sum of number is :",total_sum)
