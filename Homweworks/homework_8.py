import sqlite3


def get_books_by_author(author):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, author, publication_year
        FROM books
        WHERE author = ?
        ORDER BY name ASC
    """, (author,))

    books = cursor.fetchall()

    conn.close()

    if books:
        for book in books:
            print(book)
    else:
        print("Книги этого автора не найдены")


if __name__ == "__main__":
    get_books_by_author("J.K. Rowling")