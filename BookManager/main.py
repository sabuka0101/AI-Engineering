"""Book management console application.

Lets the user add, view, search and delete books.
Books are saved to a JSON file, so they stay after the program closes.
"""

from datetime import datetime
import json

FILE_PATH = "BookManager/books.json"


class Book:
    """Base class for every book: title, author and publication year."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @property
    def title(self):
        """Returns the book's title."""
        return self.__title

    @title.setter
    def title(self, value):
        """Sets the title. It can't be empty."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title can't be empty")
        self.__title = value.strip()

    @property
    def author(self):
        """Returns the book's author."""
        return self.__author

    @author.setter
    def author(self, value):
        """Sets the author. It can't be empty."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Author can't be empty")
        self.__author = value.strip()

    @property
    def year(self):
        """Returns the publication year."""
        return self.__year

    @year.setter
    def year(self, value):
        """Sets the year. It must be a whole number between 0 and the current year."""
        if not isinstance(value, int):
            raise ValueError("Year must be a number")
        if not 0 <= value <= datetime.now().year:
            raise ValueError(f"Year must be between 0 and {datetime.now().year}")
        self.__year = value

    def to_dict(self):
        """Returns the shared book data as a dictionary, for saving to JSON."""
        return {"title": self.title, "author": self.author, "year": self.year}

    def __str__(self):
        """Returns a readable description of the book."""
        return f"{self.title} — {self.author} ({self.year})"


class EBook(Book):
    """An electronic book. Adds a file size in megabytes."""

    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    @property
    def file_size_mb(self):
        """Returns the file size in MB."""
        return self.__file_size_mb

    @file_size_mb.setter
    def file_size_mb(self, value):
        """Sets the file size. It must be a positive number."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("File size must be a positive number")
        self.__file_size_mb = value

    def to_dict(self):
        """Adds the book type and file size to the parent's dictionary."""
        data = super().to_dict()
        data["type"] = "ebook"
        data["file_size_mb"] = self.file_size_mb
        return data

    def __str__(self):
        """Overrides the parent's __str__ (polymorphism)."""
        return f"[E-Book] {self.title} — {self.author} ({self.year}), {self.file_size_mb} MB"


class PrintedBook(Book):
    """A printed book. Adds the number of pages."""

    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    @property
    def pages(self):
        """Returns the number of pages."""
        return self.__pages

    @pages.setter
    def pages(self, value):
        """Sets the number of pages. It must be a positive whole number."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Pages must be a positive whole number")
        self.__pages = value

    def to_dict(self):
        """Adds the book type and page count to the parent's dictionary."""
        data = super().to_dict()
        data["type"] = "printed"
        data["pages"] = self.pages
        return data

    def __str__(self):
        """Overrides the parent's __str__ (polymorphism)."""
        return (
            f"[Printed] {self.title} — {self.author} ({self.year}), {self.pages} pages"
        )


class BookManager:
    """Manages the list of books and saves it to the JSON file."""

    def __init__(self):
        self.__books = []
        self.load_books()

    def add_book(self, book):
        """Adds a book to the list and saves the file."""
        self.__books.append(book)
        self.save_books()
        print(f"Added new book: {book}")

    def show_books(self):
        """Prints every book. Each type prints its own way (polymorphism)."""
        if not self.__books:
            print("No books yet.")
            return
        for number, book in enumerate(self.__books, start=1):
            print(f"{number}. {book}")

    def search_by_title(self, title):
        """Prints every book whose title contains the given text (case-insensitive)."""
        found = False
        for book in self.__books:
            if title.lower() in book.title.lower():
                print(book)
                found = True
        if not found:
            print("No book found with that title.")

    def delete_book(self, title):
        """Deletes the book with exactly this title (case-insensitive) and saves the file."""
        for book in self.__books:
            if book.title.lower() == title.lower():
                self.__books.remove(book)
                self.save_books()
                print(f"Deleted: {book}")
                return
        print("No book found with that title.")

    def clear_library(self):
        """Removes all books and empties the JSON file."""
        self.__books.clear()
        self.save_books()
        print("Library cleared.")

    def save_books(self):
        """Writes all books to the JSON file (creates or overwrites it)."""
        data = [book.to_dict() for book in self.__books]
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def load_books(self):
        """Loads books from the JSON file, if it exists."""
        try:
            with open(FILE_PATH, "r", encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            return
        except json.JSONDecodeError as error:
            print(f"Could not load books: {error}")
            return

        for item in data:
            try:
                if item["type"] == "ebook":
                    book = EBook(
                        item["title"],
                        item["author"],
                        item["year"],
                        item["file_size_mb"],
                    )
                else:
                    book = PrintedBook(
                        item["title"], item["author"], item["year"], item["pages"]
                    )
                self.__books.append(book)
            except (KeyError, ValueError) as error:
                print(f"Skipped a broken book entry: {error}")


def show_menu():
    """Prints the main menu."""
    print("\n1. Add book")
    print("2. Show books")
    print("3. Search by title")
    print("4. Delete book")
    print("5. Clear library")
    print("6. Exit")


def add_book_from_input(manager):
    """Asks the user for book details, creates the right book type and adds it."""
    print("1. E-book")
    print("2. Printed book")
    book_type = input("Choose book type: ")
    if book_type not in ("1", "2"):
        print("Error: Please choose 1 or 2")
        return

    title = input("Title: ")
    author = input("Author: ")

    try:
        year = int(input("Year: "))
    except ValueError:
        print("Error: Year must be a whole number")
        return

    try:
        if book_type == "1":
            size = float(input("File size (MB): "))
            book = EBook(title, author, year, size)
        else:
            pages = int(input("Pages: "))
            book = PrintedBook(title, author, year, pages)
        manager.add_book(book)
    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    manager = BookManager()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_book_from_input(manager)

        elif choice == "2":
            manager.show_books()

        elif choice == "3":
            title = input("Search title: ")
            if title.strip():
                manager.search_by_title(title.strip())
            else:
                print("Error: Search text can't be empty")

        elif choice == "4":
            title = input("Title of the book to delete: ")
            manager.delete_book(title.strip())

        elif choice == "5":
            confirm = input("Delete ALL books? (y/n): ")
            if confirm.lower() == "y":
                manager.clear_library()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Please choose 1–6.")
