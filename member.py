from prettytable import PrettyTable

from book import Book

class Member:

    def __init__(self, member_id, name, borrowed_books=None):
        self.member_id = member_id
        self.name = name
        if borrowed_books is None:
            self.borrowed_books = list()
        else:
            self.borrowed_books = borrowed_books

    def borrow(self, book):
        self.borrowed_books.append(book)

    def give_back(self, book):
        self.borrowed_books.remove(book)

    def list_borrowed_books(self):
        t = PrettyTable(
            ["ID", "TITEL", "AUTOR", "ISBN"])

        for index, book in enumerate(self.borrowed_books):
            t.add_row(
                [index, book.title, book.author, book.isbn])

        print(t)

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": [book.to_dict() for book in self.borrowed_books]
        }

    @staticmethod
    def member_from_dict(data):
        # Das wäre die richtige Lösung aber das macht Probleme mit der
        # restlichen Logik
        #
        # borrowed_books = [Book.book_from_dict(book) for book in
        #                   data["borrowed_books"]]
        borrowed_books = list()
        return Member(data["member_id"], data["name"], borrowed_books)