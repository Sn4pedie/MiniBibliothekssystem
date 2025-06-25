from prettytable import PrettyTable

from book import Book

class Member:
    """
    Die Member-Klasse repräsentiert ein Mitglied der Bibliothek mit Namen und ausgeliehenen Büchern.
    """

    def __init__(self, member_id, name, borrowed_books=None):
        """
        Initialisiert ein Mitglied.
        :param member_id: Eindeutige ID des Mitglieds
        :param name: Name des Mitglieds
        :param borrowed_books: Liste ausgeliehener Bücher
        """
        self.member_id = member_id
        self.name = name
        if borrowed_books is None:
            self.borrowed_books = list()
        else:
            self.borrowed_books = borrowed_books

    def borrow(self, book):
        """
        Fügt ein ausgeliehenes Buch zur Liste hinzu.
        :param book: Das Buch, das ausgeliehen wird
        """
        self.borrowed_books.append(book)

    def give_back(self, book):
        """
        Entfernt ein Buch aus der Liste der ausgeliehenen Bücher.
        :param book: Das Buch, das zurückgegeben wird
        """
        self.borrowed_books.remove(book)

    def list_borrowed_books(self):
        """
        Zeigt alle vom Mitglied ausgeliehenen Bücher als Tabelle an.
        """
        t = PrettyTable(
            ["ID", "TITEL", "AUTOR", "ISBN"])

        for index, book in enumerate(self.borrowed_books):
            t.add_row(
                [index, book.title, book.author, book.isbn])

        print(t)

    def to_dict(self):
        """
        Wandelt das Member-Objekt in ein Dictionary um.
        :return: Dictionary mit Mitgliedsdaten
        """
        return {
            "member_id": self.member_id,
            "name": self.name,
            "borrowed_books": [book.to_dict() for book in self.borrowed_books]
        }

    @staticmethod
    def member_from_dict(data):
        """
        Erstellt ein Member-Objekt aus einem Dictionary.
        (Aktuell werden ausgeliehene Bücher als leere Liste geladen, siehe Kommentar)
        :param data: Dictionary mit Mitgliedsdaten
        :return: Member-Objekt
        """
        # Das wäre die richtige Lösung aber das macht Probleme mit der
        # restlichen Logik
        #
        # borrowed_books = [Book.book_from_dict(book) for book in
        #                   data["borrowed_books"]]
        borrowed_books = list()
        return Member(data["member_id"], data["name"], borrowed_books)