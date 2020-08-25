class BookReader:
    # Maintain class
    def __init__(self, library):
        self.library = library
        self.current_book = None
        self.current_page = None

    def open_book(self, book_id):
        self.current_book = self.library.get_book(book_id)
        self.current_page = self.current_book.current_page

    def close_book(self, book_id):
        self.library.close_book(book_id)
        self.current_book = None
        self.current_page = None

    def get_book_list_by(self, key, value):
        self.library.lookup(key, value)


class Library:
    def __init__(self, books):
        self.books = books


class Book:
    def __init__(
            self, id, name, author,
            page_number, language, path,
            bookmarks, current_page
            ):
        self.id = id
        self.name = name
        self.author = author
        self.page_number = page_number
        self.language = language

        self.path = path
        self.descriptor = None

        self.bookmarks = bookmarks
        self.current_page = current_page

    def open(self):
        self.descriptor = open(self.path)
        self.__set_page(self.descriptor)
        return self.descriptor

    def close(self):
        self.__save_bookmarks()
        self.descriptor.close()

    def __save_bookmarks(self):
        pass

    def add_bookmark(self, page_number, description=None):
        bookmark = self.create_book_mark(self, page_number, description)
        self.bookmarks.append(bookmark)

    def create_book_mark(self, book, page_number, description):
        return Bookmark(book.id, page_number, description)

    def remove_bookmark(self, bookmark_id):
        del self.bookmarks[bookmark_id]

    def __set_page(self, book):
        pass


class Bookmark:
    id_counter = -1

    def __init__(self, book_id, page_number, description=None):
        self.id = self.__get_id()
        self.book_id = book_id
        self.page_number = page_number
        self.description = description

    def __get_id(self):
        Bookmark.id_counter += 1
        return Bookmark.id_counter
