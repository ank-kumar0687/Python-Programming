# Write a program to create a list and perform various operations on list 
# using menu.



lst = []

while True:
    print("\n--- LIST OPERATIONS MENU ---")
    print("1. Create list")
    print("2. Add element")
    print("3. Delete element")
    print("4. Display list")
    print("5. Search element")
    print("6. Sort list")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    
    if choice == 1:
        lst = []
        n = int(input("How many elements? "))
        for i in range(n):
            value = int(input(f"Enter element {i+1}: "))
            lst.append(value)
        print("List created successfully.")


    elif choice == 2:
        value = int(input("Enter element to add: "))
        lst.append(value)
        print("Element added.")

    
    elif choice == 3:
        value = int(input("Enter element to delete: "))
        if value in lst:
            lst.remove(value)
            print("Element deleted.")
        else:
            print("Element not found.")

    
    elif choice == 4:
        print("Current List:", lst)

    
    elif choice == 5:
        value = int(input("Enter element to search: "))
        if value in lst:
            print("Element found at index", lst.index(value))
        else:
            print("Element not found.")

    
    elif choice == 6:
        lst.sort()
        print("List sorted.")

    
    elif choice == 7:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")