def read_line_by_line():
    try:
        #opens the file in read mode
        with open("ABC.txt","r") as file:
            #read and print each line
            for line in file:
                print(line.strip()) #.strip() removes any trailing or leading white spaces
    except FileNotFoundError:

        print("The file 'ABC.txt' was not found.")
    except Exception as e:
        print(f"An error occured :{e}")

read_line_by_line()
