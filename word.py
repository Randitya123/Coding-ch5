dict={}
while True:
    print("Mini Dictonary App: \n 1.Add/Update a word\n 2.Retrieve a words definiton \n 3.Delete a word \n 4.View all words \n 5.Exit")
    user=(input("Choose an option 1-5:"))
    #add words
    if user=="1":
        newword=(input("What is the word you want: "))
        meaing=(input("What is the meaning of the word: "))
        dict[newword]=meaing
        print(newword+" added to the dictionary")
    elif user=="2":
        findword=(input("What is the word you want to find: "))
        print(findword+":"+dict[findword])
    elif user=="3":
        delword=(input("What is the word you want to delete: "))
        dict.pop(delword)
    elif user=="4":
        for i in dict:
            print(i+":"+dict[i])
    elif user=="5":
        print("Bye Bye")
        break
    else:
        print("Invalid choice")