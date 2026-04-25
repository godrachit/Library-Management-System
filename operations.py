from library.data import library_books, issued_books
from library.fine import calculate_fine
from datetime import datetime

def show_books():
    print("\nAvailable Books:")
    for book, info in library_books.items():
        status = "Available" if info["available"] else "Issued"
        print(f"- {book} [{status}]")


def issue_book():
    name = input("Enter student name: ")
    book = input("Enter book name: ")

    if book in library_books and library_books[book]["available"]:
        days = int(input("For how many days: "))
        date = datetime.now()

        issued_books[book] = {
            "student": name,
            "days": days,
            "date": date
        }

        library_books[book]["available"] = False

        print(f"\nBook issued to {name}")
        print("⚠ Fine Rule: After due date →")
        print("Week1: ₹10/day | Week2: ₹20/day | Week3: ₹60/day ...")

    else:
        print("Book not available!")


def return_book():
    book = input("Enter book name to return: ")

    if book in issued_books:
        record = issued_books[book]
        issue_date = record["date"]
        allowed_days = record["days"]

        actual_days = (datetime.now() - issue_date).days
        late_days = actual_days - allowed_days

        if late_days > 0:
            fine = calculate_fine(late_days)
            print(f"Late by {late_days} days")
            print(f"Fine: ₹{fine}")
        else:
            print("Returned on time")

        library_books[book]["available"] = True
        del issued_books[book]

    else:
        print("No such issued book!")

def add_book():
    book = input("Enter new book name: ")

    if book in library_books:
        print("Book already exists!")
    else:
        library_books[book] = {"available": True}
        print(f"'{book}' added to library")


def remove_book():
    book = input("Enter book name to remove: ")

    if book in library_books:
        if not library_books[book]["available"]:
            print("Cannot remove issued book!")
        else:
            del library_books[book]
            print(f"'{book}' removed from library")
    else:
        print("Book not found!")

def view_issued_books():
    from datetime import datetime
    from library.data import issued_books

    if not issued_books:
        print("No books issued yet.")
        return

    print("\nIssued Books Details:")
    print("--------------------------------------")

    for book, record in issued_books.items():
        student = record["student"]
        issue_date = record["date"]
        allowed_days = record["days"]

        days_passed = (datetime.now() - issue_date).days
        remaining_days = allowed_days - days_passed

        print(f"Book: {book}")
        print(f"Student: {student}")
        print(f"Issued Days: {allowed_days}")

        if remaining_days > 0:
            print(f"Return in: {remaining_days} days")
        else:
            print(f"Overdue by: {abs(remaining_days)} days")

        print("--------------------------------------")