while True:
    print("===== MAIN MENU ====")
    print("1. List Operations")
    print("2. Tuple Operations")
    print("3. Dictionary Operations")
    print("4. Set operations")
    print("5. Exit")
    user=int(input("Choice:"))
    if user==1:
        l1=[]
        while True:
            print("--- List Menu ---")
            print("1. Add element")
            print("2. Remove element")
            print("3. Display list")
            print("4. Back to main menu")
            user1=int(input("Choice:"))
            if user1==1:
                user2=int(input("What do you want to add:"))
                l1.append(user2)
            elif user1==2:
                user2=int(input("What do you want to remove:"))
                l1.remove(user2)
            elif user1==3:
                print(l1)
            elif user1==4:
                break
    elif user==2:
        t1=()
        while True:
            print("--- Tuple Menu ---")
            print("1. Create tuple")
            print("2. Display tuple")
            print("3. Count element")
            print("4. Back to main menu")
            user1=int(input("Choice:"))
            if user1==1:
                userr=(input("Enter elemants sperated by space:"))
                t1=tuple(userr.split())
            elif user1==2:
                print(t1)
            elif user1==3:
                dt=len(t1)
                print(dt)
            elif user1==4:
                break




