# Mini-Bibliothekssystem

Dieses Projekt wurde im Rahmen einer Abschlussarbeit für eine Weiterbildung entwickelt. Ziel war es, ein einfaches Verwaltungssystem für eine kleine Bibliothek zu erstellen. Im Mittelpunkt steht die Verwaltung von Büchern – insbesondere deren Lagerstatus und eventuelle Ausleihe.

## Projektbeschreibung

Das Mini-Bibliothekssystem ermöglicht:

- Das Anzeigen aller Bücher inklusive ihres aktuellen Ausleihstatus
- Das Ausleihen eines Buchs an ein Mitglied
- Das Zurückgeben eines Buchs
- (Optional) Die Verwaltung und Anzeige von Mitgliedern

Das System ist als Konsolenanwendung umgesetzt und richtet sich an Anfänger im Bereich objektorientierte Programmierung mit Python.

## Voraussetzungen und Aufbau

### 1. Klasse `Buch`

Die Klasse `Buch` bildet die Basis des Systems. Sie verfügt über folgende Attribute:

- `titel` (str): Titel des Buchs
- `autor` (str): Autor des Buchs
- `isbn` (str): ISBN-Nummer
- `lagerplatz` (str): Lagerort des Buchs
- `ausgeliehen_an` (str, int oder None): Name oder Nummer des Mitglieds, das das Buch aktuell ausgeliehen hat (oder None, falls verfügbar)

Methoden:

- `ausleihen(mitgliedsname)`: Verleiht das Buch an ein Mitglied
- `zurueckgeben()`: Gibt das Buch zurück
- Optional: `display_info()`: Zeigt Details zum Buch an

### 2. Datenstrukturen

- Eine Liste von `Buch`-Objekten zur Verwaltung aller Bücher
- Ein Dictionary für Mitglieder: Key = Name oder Nummer des Mitglieds, Value = Liste ausgeliehener Bücher
    - Alternativ (optional): Eine eigene Klasse `Mitglied` mit Attributen und Methoden

### 3. Menü und Funktionen

Über ein Konsolenmenü können folgende Aktionen ausgeführt werden:

- Bücher anzeigen (inkl. Ausleihstatus)
- Buch ausleihen
- Buch zurückgeben
- Optional: Mitglieder anzeigen

### 4. Technische Anforderungen

- Verwendung von `input()` und `print()` für die Benutzereingabe und -ausgabe
- Bedingungen (`if`, `else`)
- Schleifen (`for`, `while`)
- Listen und ggf. Dictionaries
- Einfache Fehlerbehandlung mit `try/except`
- Saubere Benennung und Struktur gemäß [PEP-8](https://www.python.org/dev/peps/pep-0008/)

### 5. Optionale Erweiterungen (für Fortgeschrittene)

- Implementierung einer Klasse `Mitglied` mit den Attributen `name`, `mitgliedsnummer`, `ausgeliehene_buecher`
- Methoden wie `buch_ausleihen()` und `buch_zurueckgeben()` in der Klasse `Mitglied`

## Nutzung

1. Das Skript mit Python ausführen:
   ```bash
   python bibliothek.py
   ```
2. Den Anweisungen im Menü folgen

## Beispielhafter Ablauf

1. Start des Programms: Das Menü erscheint
2. Auswahl „Bücher anzeigen“: Alle Bücher werden mit Titel, Autor, Lagerplatz und Status angezeigt
3. Auswahl „Buch ausleihen“: Ein Buch wird einem Mitglied zugeordnet
4. Auswahl „Buch zurückgeben“: Der Ausleihstatus wird zurückgesetzt

## Hinweise

- Das Projekt dient als Lern- und Übungsbeispiel für objektorientierte Programmierung und grundlegende Python-Konzepte.
- Die Funktionen können beliebig erweitert oder angepasst werden.
