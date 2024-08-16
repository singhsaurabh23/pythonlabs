def is_armstrong(number):
    #store the original number
    original_number=number

    #find the length of the string
    num_length=len(str(number))

    #intialising the sum of powers

    sum_of_powers=0

    #while loop to traverse each digit

    while number>0:
        digit=number%10
        sum_of_powers+=digit**num_length
        number//=10

    return sum_of_powers==original_number

user_input=int(input("Enter a number:"))
#check if a number is an armstrong number
if is_armstrong(user_input):
    print(f"{user_input} is an Armstrong number")

else:
    print(f"{user_input} is not an Armstrong number")
                     
