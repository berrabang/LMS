import psycopg2


# Funktion för att skapa en anslutning till databasen
def get_db_connection():
    return psycopg2.connect(
        dbname="library_db",
        user="postgres",
        password="Lilleskutt390023",  # Ersätt med ditt riktiga lösenord
        host="localhost",
        port="5432"
    )


# Funktion för att hämta alla böcker
def fetchall_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book;")
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books


# Funktion för att lägga till en bok
def add_book(title, author, publisher):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO book (title, author, publisher) VALUES (%s, %s, %s)",
        (title, author, publisher)
    )
    conn.commit()
    cursor.close()
    conn.close()


# Funktion för att ta bort en bok med ett specifikt ID
def delete_book_by_id(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE id = %s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()


# Funktion för att uppdatera en bok
def update_book(book_id, title, author, publisher):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE book SET title = %s, author = %s, publisher = %s WHERE id = %s",
        (title, author, publisher, book_id)
    )
    conn.commit()
    cursor.close()
    conn.close()


# SQL-querys för filtrering
def get_books_by_author_name(author):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM book WHERE author = %s;", (author,))
    books = cursor.fetchall()
    cursor.close()
    conn.close()
    return books


def get_publishers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT publisher FROM book;")
    publishers = cursor.fetchall()
    cursor.close()
    conn.close()
    return publishers


def get_all_members():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM member;")
    members = cursor.fetchall()
    cursor.close()
    conn.close()
    return members


# Funktion för att hämta alla medlemmar som har lånat en viss bok
def get_all_members_by_book(book_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    SELECT member.id, member.name 
    FROM member
    JOIN loan ON member.id = loan.member_id
    WHERE loan.book_id = %s;
    """

    cursor.execute(query, (book_id,))
    members = cursor.fetchall()

    cursor.close()
    conn.close()

    return members  # Returnerar en lista med tuples (id, namn)


# Funktion för att hämta alla lån
def get_all_loans():
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM loan;"

    cursor.execute(query)
    loans = cursor.fetchall()

    cursor.close()
    conn.close()

    return loans  # Returnerar en lista med tuples (id, book_id, member_id, loan_date, return_date)

