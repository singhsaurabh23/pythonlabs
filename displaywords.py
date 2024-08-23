def display_words():
    try:
        with open("story.txt","r") as file:
            #read line by line
            for line in file:
                words =line.split()

                for word in words:
                    if len(word)<4:
                        print(word)
    except FileNotFoundError:
        print(" the file named 'story.txt' does not exists")

    except Exception as e:
        print(f"An error occured:{e}")

display_words()
        
