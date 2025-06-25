class Book:

    def __init__(self, title, author, isbn, storage_location, borrowed_from=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.storage_location = storage_location
        self.borrowed_from = borrowed_from

    def borrow(self, member_id):
        self.borrowed_from = member_id

    def give_back(self):
        self.borrowed_from = None

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "storage_location": self.storage_location,
            "borrowed_from": self.borrowed_from
        }

    @staticmethod
    def book_from_dict(data):
        return Book(data["title"], data["author"], data["isbn"],
                    data["storage_location"], data["borrowed_from"])