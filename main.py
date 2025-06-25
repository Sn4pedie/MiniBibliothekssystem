import random

from prettytable import PrettyTable

from book import Book
from member import Member
import utility


class Library:
    """
    Die Library-Klasse repräsentiert das Mini-Bibliothekssystem und verwaltet Bücher und Mitglieder.
    """

    book_list = list()
    member_list = list()

    def menu(self):
        """
        Zeigt das Hauptmenü an und verarbeitet die Benutzerauswahl.
        """
        while True:
            print("\nMini-Bibliothekssystem")
            print("1. Alle Bücher anzeigen")
            print("2. Alle Mitglieder anzeigen")
            print("3. Programm beenden")

            eingabe = input("Wähle eine Option (1-3): ")

            if eingabe == '1':
                self.list_books()
            elif eingabe == '2':
                self.list_member()
            elif eingabe == '3':
                close_programm()
                break
            else:
                print("Ungültige Auswahl. Bitte nochmal versuchen.")

    def list_books(self):
        """
        Zeigt alle Bücher an und bietet Auswahlmöglichkeiten zur weiteren Bearbeitung.
        """
        if not self.book_list:
            print("Keine Bücher gespeichert.")
            return

        t = PrettyTable(
            ["ID", "TITEL", "AUTOR", "ISBN", "LAGERPLATZ", "AUSGELIEHEN VON"])

        for index, book in enumerate(self.book_list):
            t.add_row(
                [index, book.title,
                 book.author,
                 book.isbn,
                 book.storage_location,
                 book.borrowed_from])

        print(t)
        print("Eingabe: 0 -> Hauptmenü, 1 -> Buch verleihen, 2 -> Buch zurücknehmen, 3 -> Buch löschen, 4 -> Buch anlegen\n")

        while True:
            eingabe = input("Was möchtest du machen? ")
            if eingabe == "1" or eingabe == "2" or eingabe == "3":
                user_input_id = input("Gib ID ein: ")
                if utility.check_if_empty(user_input_id):
                    print("Ungültige Eingabe.")
                    continue
                try:
                    user_input_book = self.book_list[int(user_input_id)]

                    if eingabe == "1":
                        self.give_out(user_input_book)
                        break
                    elif eingabe == "2":
                        self.get_back(user_input_book, "books")
                        break
                    else:
                        self.remove_book(user_input_book)
                        break
                except IndexError:
                    print("Die eingegebene ID wurde nicht gefunden!")
                    continue

            if eingabe == "0":
                self.menu()
                break
            elif eingabe == "4":
                self.add_book()
                break
            else:
                print("Ungültige Eingabe!")

    def list_member(self, only_list=False):
        """
        Zeigt alle Mitglieder an und bietet Auswahlmöglichkeiten zur weiteren Bearbeitung.
        :param only_list: Wenn True, werden keine weiteren Optionen angezeigt.
        """
        if not self.member_list:
            print("Keine Mitglieder gespeichert.")
            return

        t = PrettyTable(
            ["MEMBER ID", "NAME"])

        for member in self.member_list:
            t.add_row(
                [member.member_id, member.name])

        print(t)

        if only_list is False:
            print("Eingabe: 0 -> Hauptmenü, 1 -> Bücher anzeigen, 2 -> Mitglied löschen, 3 -> Mitglied anlegen\n")

            while True:
                eingabe = input("Was möchtest du machen? ")
                if eingabe == "1" or eingabe == "2":
                    user_input_id = input("Mitgliedsnummer eingeben: ")
                    user_input_member = ""
                    if any(member.member_id == user_input_id for member in self.member_list):
                        for member in self.member_list:
                            if member.member_id == user_input_id:
                                user_input_member = member

                        if eingabe == "1":
                            self.list_member_books(user_input_member)
                            break
                        else:
                            self.remove_member(user_input_member)
                            break
                    else:
                        print("Eingegebene Mitgliedsnummer wurde nicht gefunden!")
                        continue

                if eingabe == "0":
                    self.menu()
                    break
                elif eingabe == "3":
                    self.add_member()
                    break
                else:
                    print("Ungültige Eingabe!")

    def list_member_books(self, member):
        """
        Zeigt alle ausgeliehenen Bücher eines Mitglieds an und bietet Optionen zur Rückgabe.
        :param member: Das Mitglied, dessen Bücher angezeigt werden.
        """
        member.list_borrowed_books()
        print("Eingabe: 0 -> Hauptmenü, 1 -> Buch zurückgeben, 2 -> Mitglieder anzeigen\n")
        while True:
            eingabe = input("Was möchtest du machen? ")
            if eingabe == "1":
                user_input_id = input("Gib ID ein: ")
                try:
                    # Buch anhand der Liste ausgeliehener Bücher auswählen
                    user_input_book = member.borrowed_books[int(user_input_id)]
                    self.get_back(user_input_book, "member_books")
                    break
                except IndexError:
                    print("Die eingegebene ID wurde nicht gefunden!")
                    continue

            if eingabe == "0":
                self.menu()
                break
            elif eingabe == "2":
                self.list_member()
                break
            else:
                print("Falsche Eingabe!")

    def add_book(self):
        """
        Legt ein neues Buch anhand von Nutzereingaben an und fügt es der Bibliothek hinzu.
        """
        title_ok = author_ok = isbn_ok = storage_location_ok = False
        new_title = new_author = new_isbn = new_storage_location = ""

        while True:
            if not title_ok:
                title = input("Gebe den Titel ein: ")
                if utility.check_if_empty(title):
                    print("Titel darf nicht leer sein.")
                    continue
                else:
                    new_title = title
                    title_ok = True

            if not author_ok:
                author = input("Gebe den Autor ein: ")
                if utility.check_if_empty(author):
                    print("Autor darf nicht leer sein.")
                    continue
                else:
                    new_author = author
                    author_ok = True

            if not isbn_ok:
                isbn = input("Gebe die Isbn ein: ")
                if utility.check_if_empty(isbn):
                    print("Isbn darf nicht leer sein.")
                    continue
                else:
                    new_isbn = isbn
                    isbn_ok = True

            if not storage_location_ok:
                storage_location = input("Gebe die Lagerposition ein: ")
                # Lagerplatz muss eindeutig und nicht leer sein
                if utility.check_if_empty(storage_location) or \
                        any(book.storage_location == storage_location
                            for book in self.book_list):
                    print("Lagerplatz darf nicht leer oder vergeben sein.")
                    continue
                else:
                    new_storage_location = storage_location
                    break

        self.book_list.append(
            Book(new_title, new_author, new_isbn, new_storage_location))

    def remove_book(self, book):
        """
        Entfernt ein Buch aus der Bibliothek und aktualisiert ggf. das Mitglied.
        :param book: Das zu entfernende Buch.
        """
        for member in self.member_list:
            if member.member_id == book.borrowed_from:
                member.give_back(book)

        self.book_list.remove(book)
        self.list_books()

    def add_member(self):
        """
        Legt ein neues Mitglied anhand von Nutzereingaben an und fügt es der Bibliothek hinzu.
        """
        new_name = ""
        new_member_id = 00000
        name_ok = False
        while True:
            if not name_ok:
                name = input("Gebe den Namen ein: ")
                if utility.check_if_empty(name):
                    print("Name darf nicht leer sein!")
                    continue
                else:
                    new_name = name
                    name_ok = True

            # Zufällige 5-stellige Mitgliedsnummer generieren
            member_id = ''.join(random.choices('0123456789', k=5))
            # Sicherstellen, dass die Mitgliedsnummer einzigartig ist
            if any(member.member_id == member_id for member in
                   self.member_list):
                continue
            else:
                new_member_id = member_id
                break

        self.member_list.append(Member(new_member_id, new_name))

    def remove_member(self, member):
        """
        Entfernt ein Mitglied aus der Bibliothek und setzt ausgeliehene Bücher zurück.
        :param member: Das zu entfernende Mitglied.
        """
        for book in self.book_list:
            if book.borrowed_from == member.member_id:
                book.borrowed_from = None

        self.member_list.remove(member)
        self.list_member()

    def give_out(self, book):
        """
        Verleiht ein Buch an ein Mitglied.
        :param book: Das zu verleihende Buch.
        """
        if book.borrowed_from is None:
            self.list_member(True)
            member_id = input("Gebe eine Mitgliedsnummer ein: ")

            if any(member.member_id == member_id for member in self.member_list):
                for member in self.member_list:
                    if member.member_id == member_id:
                        member.borrow(book)
                        book.borrowed_from = member_id
            else:
                print("Eingegebene Mitgliedsnummer wurde nicht gefunden!")
        else:
            print("Buch bereits ausgeliehen!")

        self.list_books()

    def get_back(self, book, redirect):
        """
        Nimmt ein Buch zurück und gibt es für Ausleihe frei.
        :param book: Das zurückgegebene Buch.
        :param redirect: Bestimmt, wohin nach Rückgabe weitergeleitet wird.
        """
        member_redirect = ""
        for member in self.member_list:
            if member.member_id == book.borrowed_from:
                member_redirect = member
                member.give_back(book)

        book.borrowed_from = None

        if redirect == "books":
            self.list_books()
        else:
            self.list_member_books(member_redirect)

    def import_data(self):
        """
        Importiert Bücher- und Mitgliederdaten aus Dateien.
        """
        result = utility.read_file()
        self.book_list = result["books"]
        self.member_list = result["members"]

    def export_data(self):
        """
        Exportiert Bücher- und Mitgliederdaten in Dateien.
        """
        utility.save_file(self.book_list, self.member_list)


def close_programm():
    """
    Beendet das Programm und speichert die aktuellen Daten.
    """
    print("Programm wird beendet ...")
    library.export_data()
    quit()


if __name__ == "__main__":
    try:
        library = Library()
        library.import_data()
        library.menu()
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt! ", end="")
        close_programm()
    except Exception as e:
        print("Das Programm wurde unerwartet beendet!\n", e)