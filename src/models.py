from dataclasses import dataclass
from src.custom_exceptions import BookNotFoundError, BookAlreadyBorrowedError


@dataclass
class Book:
    title: str
    author: str
    isbn: str
    is_borrowed: bool


class User:
    name: str
    borrowed_books: list[Book]


@dataclass
class Library:
    books: list[Book]
    users: list[User]

    def borrow_book(self, user: User, book: Book) -> None:
        if book not in self.books:
            raise BookNotFoundError
        if book.is_borrowed:
            raise BookAlreadyBorrowedError()
        book.is_borrowed = True
        user.borrowed_books.append(book)

    def return_book(self, user: User, book: Book) -> None:
        if book not in user.borrowed_books:
            raise BookNotFoundError
        book.is_borrowed = False
        user.borrowed_books.remove(book)

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)
