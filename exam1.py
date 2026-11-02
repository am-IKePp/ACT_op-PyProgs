class Item:
    def __init__(self, id, name, year):
        self.id = id
        self.name = name
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.year}"

#класс книша
class Book:
    def __init__(self, id, name, year, author, isbn):
        super().__init__(id, name, year)
        self.author = author
        self.isbn = isbn
        self.status = True

    def __str__(self):
        if self.status:
            status = "доступна"
        else:
            status = "выдана"

        return f"{self.name} - {self.author} ({status})"

#класс читатель
class Reader:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = []

    def __str__(self):
        return f"Читатель: {self.name}"

#класс библиотека
class Library:
    def __init__(self):
        self.books = []
        self.readers = []

#метод добавить книгу
    def add_book(self, book):
        self.books.append(book)
        print("Книга добавлена")

#метод регистрации читателя
    def register_reader(self, reader):
        self.readers.append(reader)
        print("Читатель зарегистрирован")

#выдача книги
    def lend_book(self, book_id, reader_id):
        book = None
        reader = None

        for b in self.books:
            if b.id == book_id:
                book = b

        for r in self.readers:
            if r.id == reader_id:
                reader = r

        if book is None:
            raise ValueError("Книга не найдена")

        if reader is None:
            raise ValueError("Читатель не зарегистрирован")

        if not book.status:
            raise ValueError("Книга уже выдана")

        book.status = False
        reader.books.append(book)
        print("Книга выдана")

#возврат книги
    def return_book(self, book_id, reader_id):
        for reader in self.readers:
            if reader.id == reader_id:
                for book in reader.books:
                    if book.id == book_id:
                        book.status = True
                        reader.books.remove(book)
                        print("Книга возвращена")
                        return

        raise ValueError("Книга не найдена у читателя")

#поиск книги по автору
    def find_books_by_author(self, author):
        result = []

        for book in self.books:
            if book.author == author:
                result.append(book)

        return result

#книги читателя
    def get_reader_books(self, reader_id):
        for reader in self.readers:
            if reader.id == reader_id:
                return reader.books

        raise ValueError("Читатель не зарегистрирован")
