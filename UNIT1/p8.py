''' Write a Python program to perform following operation on given string 
input:
a) Count Number of Vowel in given string
b) Count Length of string (donot use len() )
c) Reverse string
d) Find and replace operation
e) check whether string entered is a palindrome or not'''


s = input("Enter a string: ")

while True:
    print("\n--- STRING OPERATIONS MENU ---")
    print("a. Count number of vowels")
    print("b. Count length of string (without using len())")
    print("c. Reverse the string")
    print("d. Find and replace")
    print("e. Check palindrome")
    print("f. Exit")

    choice = input("Enter your choice: ")

    # a) Count number of vowels
    if choice == 'a':
        count = 0
        for ch in s:
            if ch.lower() in 'aeiou':
                count += 1
        print("Number of vowels:", count)

    # b) Count length of string without len()
    elif choice == 'b':
        length = 0
        for _ in s:
            length += 1
        print("Length of string:", length)

    # c) Reverse string
    elif choice == 'c':
        rev = ""
        for ch in s:
            rev = ch + rev
        print("Reversed string:", rev)

    # d) Find and replace
    elif choice == 'd':
        old = input("Enter character/string to find: ")
        new = input("Enter replacement: ")
        s = s.replace(old, new)
        print("Updated string:", s)

    # e) Check palindrome
    elif choice == 'e':
        rev = ""
        for ch in s:
            rev = ch + rev
        if s == rev:
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")

    # f) Exit
    elif choice == 'f':
        print("Program ended.")
        break

    else:
        print("Invalid choice! Try again.")