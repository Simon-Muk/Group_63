import sqlite3


def create_table():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    books = [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 5),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 3),
        ("War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 2),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Novel", 671, 4),
        ("The Alchemist", "Paulo Coelho", 1988, "Adventure", 208, 6),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 320, 7),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 180, 5),
        ("Moby Dick", "Herman Melville", 1851, "Adventure", 635, 2),
        ("Brave New World", "Aldous Huxley", 1932, "Sci-Fi", 268, 4),
        ("The Little Prince", "Antoine de Saint-Exupéry", 1943, "Fairy tale", 96, 8)
    ]

    cursor.executemany("""
    INSERT INTO books
    (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    insert_books()
    print("Таблица создана и книги добавлены!")

