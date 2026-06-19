# Library Book Management System

library = {}

while True:
    print("\n----- Library Menu -----")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        copies = int(input("Enter number of copies: "))
        library[book] = copies
        print("Book added successfully!")

    elif choice == "2":
        book = input("Enter book name to issue: ")

        if book in library and library[book] > 0:
            library[book] -= 1
            print("Book issued successfully!")
        else:
            print("Book not available!")

    elif choice == "3":
        book = input("Enter book name to return: ")

        if book in library:
            library[book] += 1
        else:
            library[book] = 1

        print("Book returned successfully!")

    elif choice == "4":
        print("\nAvailable Books:")

        if len(library) == 0:
            print("No books in library")
        else:
            for book, copies in library.items():
                print(book, ":", copies)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")