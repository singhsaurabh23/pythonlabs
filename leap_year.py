#input from the user for year
year = int(input("Enter the year which you want to check"))
#checking all the condition satisfying for a leap year
if (year%4==0 and year%100 !=0)or (year % 400 == 0):
#printing the desired output
    print("Year chosen is a leap year")
else:
    print("Chosen year is not a leap year")
