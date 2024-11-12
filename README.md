# Assignment

Create a Python program that simulates a simple library management system. This system should allow a user to manage book records and user interactions with the library, including borrowing and returning books. The project should make use of classes, file handling for data persistence, exception handling, and functions to perform various tasks.

1. Classes and Objects in [./src/models.py](./src/models.py):
Create classes accordingly:

`Book` class
**attributes**
- `id`: int (unique, auto-incremented)
- `title`: str
- `author`: str
- `isbn`: str
- `is_borrowed`: bool

`User` class
**attributes**
- `id`: int (unique, auto-incremented)
- `name`: str
- `borrowed_books`: list[Book]


`Library` class
**attributes**
- `books`: list[Book]
- `users`: list[User]

**methods**
- `register_user`: Register a new user
    this method should take a `User` instance as an argument and add it to the library's list of users.
- `remove_user`: Remove a user from the library
    this method should take a `User` instance as an argument and remove it from the library's list of users.
- `add_book`: Add a book to the library
    this method should take a `Book` instance as an argument and add it to the library's list of books.
- `remove_book`: Remove a book from the library
    this method should take a `Book` instance as an argument and remove it from the library's list of books.
- `lend_book`: Lend a book to a user
    this method should take a `Book` instance and a `User` instance as arguments and update the book's status to borrowed. It should also add the book to the user's borrowed_books list.
- `return_book`: Return a book to the library
    this method should take a `Book` instance and a `User` instance as arguments and update the book's status to available. It should also remove the book from the user's borrowed_books list.
- `search_book`: Search for a book in the library
    this method should take a `title` as an argument and return a list of books that match the title.
- `list_books`: List all available books in the library (not borrowed)
    this method should return a list of books that are available in the library.

2. File Handling:
each method in `Library` class should update state of the corresponding file in the `data` directory.
- `add_book`: should add a new book to the `book_catalog.csv` file
- `remove_book`: should remove a book from the `book_catalog.csv` file
- `lend_book`: should update the `book_catalog.csv` file to mark the book as borrowed
- `return_book`: should update the `book_catalog.csv` file to mark the book as available
- `register_user`: should add a new user to the `users.csv` file
- `remove_user`: should remove a user from the `users.csv` file


3. Exception Handling:
Implement exception handling in the `Library` class to handle the following cases:
- `BookNotFoundError`: raise this exception when a book is not found in the library
- `BookAlreadyBorrowedError`: raise this exception when a user tries to borrow a book that is already borrowed

4. Usage:
In `main.py` file write a program that demonstrates the usage of the `Library` class. The program should allow the user to perform the following actions:
- Add a book to the library
- Remove a book from the library
- Lend a book to a user
- Return a book to the library
- Search for a book in the library
- List all available books in the library



