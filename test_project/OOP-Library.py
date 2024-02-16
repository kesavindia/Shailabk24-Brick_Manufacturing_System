class Library:
    def __init__(self, book_list):
        self.Books_list = book_list
        self.available_books_list = book_list[:]
        self.books_lent = {}  # key-book value-username

    def display_all_books(self):
        for book in self.Books_list:
            print(book)

    def display_available_books(self):
        for book in self.available_books_list:
            print(book)

    def lending(self, name, book):
        if book not in self.Books_list:
            print("Entered book is not in the total list.")
            return
        if book in self.available_books_list:
            self.books_lent[book] = name
            self.available_books_list.remove(book)
            print(f"{book} has been successfully lent to {name}.")
        else:
            print(f"The book is already lent to {self.books_lent[book]}.")

    def return_books(self, book):
        if book in self.books_lent:
            self.available_books_list.append(book)
            del self.books_lent[book]
            print(f"{book} has been successfully returned.")
        else:
            print("This book was not borrowed.")


if __name__ == "__main__":
    lib = Library(["The Life Divine", "Da Vinci", "Anaconda", "The Game", "The Life"])
    lib2 = Library(['Mother', 'Father', 'Guru', 'God'])
    print("Welcome to the library")

    while True:
        print("1. Display the list of all books.")
        print("2. Display the list of available books.")
        print("3. Borrow a book.")
        print("4. Return a book.")
        print("5. Exit.")

        option = input("Enter an option to choose: ")

        if option == "1":
            lib.display_all_books()
        elif option == "2":
            lib.display_available_books()
        elif option == "3":
            book = input("Enter a book name: ")
            name = input("Enter your name: ")
            lib.lending(name, book)
        elif option == "4":
            book = input("Enter a book to return: ")
            lib.return_books(book)
        elif option == "5":
            break
        else:
            print("Please enter a valid number.")
