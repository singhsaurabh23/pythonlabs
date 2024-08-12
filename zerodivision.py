try:
    value1=10
    value2=10
    print(value1/value2)
except ZeroDivisionError as e:
    print("Please change value2 as we cannot divide by zero")
print("program ended")
