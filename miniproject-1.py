# create a libaray class
# display books
# lend books - (who owns the books if not present)
# add books
# retune books

# HarshLibrary = Library(listofbooks , library_name)


# dictionary (books-nameofperson)
#
# create a main function and run an infinite while loop asking
# users for their input

class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our library{self.name}")
        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
       if book not in self.lendDict.keys():
           self.lendDict.update({book: user})
           print("Book dictionary has been updated. you can take the book now")
       else:
        print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    harsh = Library(['Python', 'C++', 'Django', 'Asp.net', 'HTML', 'Jangle book'],
                    "harsh")

    while(True):
        print(f"Welcome to the {harsh.name} library. Enter Your choice to continue")
        print("1. Display Book")
        print("2. lend a book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = (input())
        if user_choice not in ['1', '2', '3', '4']:
            print("please enter a valid option")
            continue
        else:
            user_choice= int(user_choice)

        if user_choice == 1:
            harsh.displayBooks()

        elif user_choice == 2:
           book = input("Enter the name of the book you went to lend:")
           user = input("Enter your name")
           harsh.lendBook(user, book)

        elif user_choice == 3:
           book = input("Enter the name of the book you went to add:")
           harsh.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you went to add:")
            harsh.returnBook(book)

        else:
            print("Not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!= "q"):

            user_choice2 = input()
            if user_choice2 == "q":
                exit()

            elif user_choice2 == "c":
                continue


