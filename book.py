class Book:
    """
    Die Book-Klasse repräsentiert ein Buch mit Titel, Autor, ISBN, Lagerplatz und aktueller Ausleihe.
    """

    def __init__(self, title, author, isbn, storage_location, borrowed_from=None):
        """
        Initialisiert ein Buch-Objekt.
        :param title: Titel des Buchs
        :param author: Autor des Buchs
        :param isbn: ISBN-Nummer
        :param storage_location: Lagerplatz in der Bibliothek
        :param borrowed_from: Mitgliedsnummer, falls das Buch ausgeliehen ist
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.storage_location = storage_location
        self.borrowed_from = borrowed_from

    def borrow(self, member_id):
        """
        Markiert das Buch als ausgeliehen.
        :param member_id: ID des Mitglieds, das das Buch ausleiht
        """
        self.borrowed_from = member_id

    def give_back(self):
        """
        Markiert das Buch als zurückgegeben.
        """
        self.borrowed_from = None

    def to_dict(self):
        """
        Wandelt das Buch-Objekt in ein Dictionary um.
        :return: Dictionary mit Buchdaten
        """
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "storage_location": self.storage_location,
            "borrowed_from": self.borrowed_from
        }

    @staticmethod
    def book_from_dict(data):
        """
        Erstellt ein Buch-Objekt aus einem Dictionary.
        :param data: Dictionary mit Buchdaten
        :return: Book-Objekt
        """
        return Book(data["title"], data["author"], data["isbn"],
                    data["storage_location"], data["borrowed_from"])