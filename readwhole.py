def read_whole_content():
    try:
        #open the file in read mode
        with open("ABC.txt", "r") as file:
            #read the entire file content
            content=file.read()
            #split the content into words
            words=content.split()

            #count the number of words
            word_count=len(words)

            #display the number of words
            print(f"The number of words in the file:{word_count}")
            
    except FileNotFoundError:
        print("The file does not exists")

    except Exception as e :
        print(f"Error occured :{e}")
        
read_whole_content()
