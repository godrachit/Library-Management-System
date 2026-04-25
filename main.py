from library.operations import (
    show_books, issue_book, return_book,
    add_book, remove_book, view_issued_books
)

def main():
    while True:
        print("\n====== LIBRARY MENU ======")
        print("1. Show Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Add Book")
        print("5. Remove Book")
        print("6. View Issued Books")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_books()

        elif choice == "2":
            issue_book()

        elif choice == "3":
            return_book()

        elif choice == "4":
            add_book()

        elif choice == "5":
            remove_book()

        elif choice == "6":
            view_issued_books()

        elif choice == "7":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()