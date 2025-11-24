class Book:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def __str__(self):
        return f'"{self.get_title()}" автора {self.get_author()}'

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError(f"'{book}' не является книгой")
        self._books.append(book)

    def find_book_by_title(self, title):
        for item in self._books:
            if item.get_title() == title:
                return item
        return None

    def __len__(self):
        return len(self._books)


# Пример использования
book1 = Book("1984", "Джордж Оруэлл")
book2 = Book("Мастер и Маргарита", "Михаил Булгаков")

library = Library()
library.add_book(book1)
library.add_book(book2)

print(f"В библиотеке {len(library)} книги.")

found_book = library.find_book_by_title("1984")
if found_book:
    print(f"Найдена книга: {found_book}")

try:
    library.add_book("Не книга")
except TypeError as e:
    print(f"Ошибка добавления: {e}")

# Попытка прямого доступа к приватному атрибуту вызовет ошибку
# print(book1.__title)
