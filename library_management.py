class Library:
    def __init__(self):
        self.book = []
        self.no_of_books = 0

    def add(self, selected_book):
        self.book.append(selected_book)
        self.no_of_books += 1

    def inventory(self):
        print(f'Number of books now is {self.no_of_books}')
        if self.no_of_books > 0:
            print(f"Here are all the books in your inventory: {', '.join(self.book)}")
        else:
            print("Your inventory is empty.")

    def remove(self, remove_book):
        if remove_book in self.book:
            self.book.remove(remove_book)
            self.no_of_books -= 1
            print(f"{remove_book} removed from your inventory.")
        else:
            print(f"{remove_book} is not in your inventory.")

    def check(self):
        if self.no_of_books != len(self.book):
            raise CustomError("Something is wrong in the program!")
        else:
            print(f"{len(self.book)} = {self.no_of_books}")

# Create a single instance of Library to manage the library's state
k = Library()

print("WELCOME TO LIBRARY ---- by Ansh")
while True:
    print("\nEnter 1 to see books alloted to you")
    print("Enter 2 to add another book in your inventory")
    print("Enter 3 to remove any book from your inventory")
    print("Enter 0 to quit")

    choice = input('What would you like to do: ')

    if choice == '1':
        k.inventory()
    elif choice == '2':
        selected_book_inp = input('Enter the name of the book you want to add: ')
        k.add(selected_book_inp)
        k.inventory()
    elif choice == '3':
        remove_book_inp = input('Enter the name of the book you want to remove: ')
        k.remove(remove_book_inp)
        k.inventory()
    elif choice == '0':
        print("Thank you for using the library. Goodbye!")
        break
    else:
        print('Invalid input. Please choose from the above options.')
