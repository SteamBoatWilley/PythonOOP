# Classs => Library
# Laryers of Abstractio => display available books, to lend a book, to add a book

# Class => Customer
# Layers of abstraction => request for a book, return a book

class Library:

    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks

    def displayAvailableBooks(self):
        print()
        print("Available Books: ")
        for book in self.availableBooks:
            print(book)


    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("you have borrowed the book!")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry the book is not available in our list.")
    
    def addBook(self, returnedBook):
        self.availableBooks.append(returnedBook)
        print("you have returned the book, thank you!")


class Customer:
    def requestBook(self):
        print("Enter the name of a book you would like to borrow: ")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book which you are returning: ")
        self.book = input()
        return self.book 

library = Library(['Think and Grow Rich', 'Who Will Cry WHen you Die', 'For One More Day'])
customer = Customer()
while True:
    print("Enter 1 to display the available books")
    print("Enter 2 to request for a book")
    print("Enter 3 to return a book")
    print("Enter 4 to exit")
    userChoice = int(input())
    if userChoice is 1:
        library.displayAvailableBooks()
    elif userChoice is 2:
        requestedBook = customer.requestBook()
        library.lendBook(requestedBook)
    elif userChoice is 3:
        returnedBook = customer.returnBook()
        library.addBook(returnedBook)
    elif userChoice is 4:
        quit()
