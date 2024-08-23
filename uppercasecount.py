def count_uppercase():
    try:
        #open the file in read mode
        with open("ABC.txt","r") as file:
            #read the entire content of the file
            content =file.read()
            #initialisng a counter for each uppercase character
            uppercase_count=sum(1 for char in content if char.isupper())
            #display the number of uppercase characters
            print(f"Total uppercase words are:{uppercase_count}")

    except FileNotFoundError:
        print("The file 'ABC.txt' does not exists")

    except Exception as e:
        print(f"An error occured:{e}")

count_uppercase()
