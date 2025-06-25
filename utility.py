import json

from book import Book
from member import Member

def read_file():
    """
    Liest Buch- und Mitgliedsdaten aus JSON-Dateien ein und stellt sie als Objekte bereit.
    :return: Dictionary mit Listen von Book- und Member-Objekten
    """
    book_list = list()
    member_list = list()
    books_from_json = do_read("mock_books.json")
    member_from_json = do_read("mock_members.json")
    for book in books_from_json:
        book_to_add = Book.book_from_dict(book)
        book_list.append(book_to_add)
    for member in member_from_json:
        member_to_add = Member.member_from_dict(member)
        member_list.append(member_to_add)

    # Workaround damit die restliche Logik funktioniert
    # da sonst das Importieren Probleme bezüglich Objektreferenzen macht
    for book in book_list:
        if book.borrowed_from is not None:
            member_id = book.borrowed_from
            for member in member_list:
                if member.member_id == member_id:
                    member.borrow(book)

    return {"books": book_list, "members": member_list}

def do_read(filename):
    """
    Liest eine JSON-Datei und gibt den Inhalt zurück.
    :param filename: Dateiname
    :return: Inhalt als Liste oder Dictionary
    """
    try:
        with open(filename, "r", encoding="utf-8") as jsonfile:
            return json.load(jsonfile)
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden!")
        return []
    except Exception as e:
        print("Unvorhergesehener Fehler aufgetreten:", e)
        return []

def save_file(book_list, member_list):
    """
    Speichert Buch- und Mitgliedsdaten als JSON-Dateien.
    :param book_list: Liste von Book-Objekten
    :param member_list: Liste von Member-Objekten
    """
    book_dict = [book.to_dict() for book in book_list]
    member_dict = [member.to_dict() for member in member_list]
    do_save("mock_books.json", book_dict)
    do_save("mock_members.json", member_dict)

def do_save(filename, data):
    """
    Speichert Daten in einer JSON-Datei.
    :param filename: Dateiname
    :param data: Zu speichernde Daten
    """
    try:
        with open(filename, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)
    except FileNotFoundError:
        print("Die Datei wurde nicht gefunden!")
    except Exception as e:
        print("Unvorhergesehener Fehler aufgetreten:", e)

def check_if_empty(user_input):
    """
    Prüft, ob eine Nutzereingabe leer ist.
    :param user_input: Nutzereingabe
    :return: True, wenn leer, sonst False
    """
    if user_input is None or user_input.strip() == "":
        return True
    else:
        return False