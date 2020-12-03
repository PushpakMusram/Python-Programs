import sys


class Library:
    def __init__(self, list_of_books):
        self.availablebooks = list_of_books

    def displayAvailablebooks(self):
        print("The books we have in our library are as follows:")
        print("================================")
        for book in self.availablebooks:
            print(book)

    def lend_Book(self, requested_Book):
        if requested_Book in self.availablebooks:
            print("The book you requested has now been borrowed")
            self.availablebooks.remove(requested_Book)
        else:
            print("Sorry the book you have requested is currently not in the library")

    def add_Book(self, returned_Book):
        self.availablebooks.append(returned_Book)
        print("Thanks for returning your borrowed book")


class Student:
    def request_Book(self):
        print("Enter the name of the book you'd like to borrow>>")
        self.book = input()
        return self.book

    def return_Book(self):
        print("Enter the name of the book you'd like to return>>")
        self.book = input()
        return self.book


def main():
    library = Library(["Munni ki Badnami","Sheela ki Jawani","Hasinao ki Manmani"])
    student = Student()
    done = False
    while done == False:
        print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
        choice = int(input("Enter Choice:"))
        if choice == 1:
            library.displayAvailablebooks()
        elif choice == 2:
            library.lend_Book(student.request_Book())
        elif choice == 3:
            library.add_Book(student.return_Book())
        elif choice == 4:
            sys.exit()


main()
