from typing import List, Optional


from database import Database
from model import Book, Publisher, Member
from utils import logger

import psycopg2
import os


def get_db_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT")
    )


class Repository:
    """
    Repository class for handling database operations related to books, publishers, members, and loans.
    """

    def __init__(self) -> None:
        """Initializes the Repository class and connects to the database."""
        self.db = Database()
        try:
            self.db.connect()
        except Exception as e:
            logger.critical(f"Failed to connect to the database: {e}")
            raise RuntimeError("Database connection failed.")

    def fetchall_books(self) -> List[Book]:
        """
        Fetches all books from the database.

        Returns:
            List[Book]: A list of Book objects representing all books in the database.
        """


        query = "SELECT id, title, author, publisher FROM book"
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM book;")
        books = cursor.fetchall()
        cursor.close()
        conn.close()

        try:
            results = self.db.fetch_results(query = query)
            return [Book(*result) for result in results]
        except Exception as e:
            logger.error(f"Failed to fetch all books: {e}")
            return []

    def add_book(self, book: Book) -> None:
        """
        Adds a new book to the database.

        Args:
            book (Book): The book object to be added.
        """
        ### YOUR QUERY ###
        # query = ...
        # params = ...
        # remove the following line after your implementation
        '''conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO book (title, author, publisher) VALUES (%s, %s, %s)",
            (title, author, publisher)
        )
        conn.commit()
        cursor.close()
        conn.close()
'''
        query = "INSERT INTO book (title, author, publisher) VALUES (%s, %s, %s)"
        params = (book.title, book.author, book.publisher)

        try:
            self.db.execute_query(query = query, params = params)
            logger.info(f"Book '{book.title}' added successfully.")
        except Exception as e:
            logger.error(f"Failed to add book '{book.title}': {e}")
            raise RuntimeError("Failed to add book.")

    def delete_book_by_id(self, book_id: int) -> None:
        """
        Deletes a book by its ID.

        Args:
            book_id (int): The ID of the book to delete.
        """
        ### YOUR QUERY ###
        # query = ...
        # params =
        # remove the following line after your implementation
        '''
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM book WHERE id = %s", (book_id,))
        conn.commit()
        cursor.close()
        conn.close()'''
        query = "DELETE FROM book WHERE id = %s"
        params = (book_id,)

        try:
            self.db.execute_query(query = query, params = params)
            logger.info(f"Book with ID {book_id} deleted successfully.")
        except Exception as e:
            logger.error(f"Failed to delete book with ID {book_id}: {e}")
            raise RuntimeError("Failed to delete book.")

    def update_book(self, book: Book) -> None:
        """
        Updates the details of a book in the database.

        Args:
            book (Book): The book object with updated information.
        """
        ### YOUR QUERY ###
        # query = ...
        # params
        # remove the following line after your implementation
        '''conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE book SET title = %s, author = %s, publisher = %s WHERE id = %s",
            (title, author, publisher, book_id)
        )
        conn.commit()
        cursor.close()
        conn.close()'''
        query = """
            UPDATE book 
            SET title = %s, author = %s, publisher = %s 
            WHERE id = %s
            """
        params = (book.title, book.author, book.publisher, book.id)

        try:
            self.db.execute_query(query = query, params = params)
            logger.info(f"Book with ID {book.id} updated successfully.")
        except Exception as e:
            logger.error(f"Failed to update book with ID {book.id}: {e}")
            raise RuntimeError("Failed to update book.")

    def get_books_by_author_name(self, author_name: str) -> List[Book]:
        """
        Fetches books by author name.

        Args:
            author_name (str): The name of the author.

        Returns:
            List[Book]: A list of books by the given author.
        """
        ### YOUR QUERY ###
        # query = ...
        # params = ...
        # remove the following line after your implementation
        '''conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM book WHERE author = %s;", (author,))
        books = cursor.fetchall()
        cursor.close()
        conn.close()'''
        query = """
            SELECT * FROM book WHERE author = %s;
            """
        params = (author_name,)

        try:
            results = self.db.fetch_results(query = query, params = params)
            return [Book(*result) for result in results]
        except Exception as e:
            logger.error(f"Failed to fetch books by author '{author_name}': {e}")
            return []

    def get_publishers(self) -> List[Publisher]:
        """
        Fetches all publishers from the database.

        Returns:
            List[Publisher]: A list of Publisher objects.
        """
        ### YOUR QUERY ###
        # query = ...
        # remove the following line after your implementation
        '''conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT publisher FROM book;")
        publishers = cursor.fetchall()
        cursor.close()
        conn.close()'''
        query = """
            SELECT DISTINCT publisher FROM book;
            """

        try:
            results = self.db.fetch_results(query = query)
            return [Publisher(*result) for result in results]
        except Exception as e:
            logger.error(f"Failed to fetch publishers: {e}")
            return []

    def get_all_members(self) -> List[Member]:
        """
        Fetches all members from the database.

        Returns:
            List[Member]: A list of Member objects.
        """
        ### YOUR QUERY ###
        # query = ...
        # remove the following line after your implementation
        '''conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM member;")
        members = cursor.fetchall()
        cursor.close()
        conn.close()'''
        query = """
            SELECT * FROM member;
            """

        try:
            results = self.db.fetch_results(query = query)
            return [Member(*result) for result in results]
        except Exception as e:
            logger.error(f"Failed to fetch members: {e}")
            return []

    def get_book_by_name(self, book_name: str) -> Optional[Book]:
        """
        Fetches a book by its title.

        Args:
            book_name (str): The title of the book.

        Returns:
            Optional[Book]: The Book object if found, otherwise None.
        """
        ### YOUR QUERY ###
        # query = ...
        # params = ...
        # remove the following line after your implementation
        #raise NotImplementedError("get_book_by_name method is not implemented.")
        query = """
            SELECT * FROM book WHERE title = %s;
            """
        params = (book_name,)
        ### YOUR CODE ###
        try:
            result = self.db.fetch_results(query = query, params = params)
            return Book(*result[0]) if result else None
        except Exception as e:
            logger.error(f"Failed to fetch book '{book_name}': {e}")
            return None

    def get_all_members_by_book(self, book_name: str) -> List[tuple]:
        """
        Fetches all members who borrowed a specific book.

        Args:
            book_name (str): The title of the book.

        Returns:
            List[tuple]: A list of tuples containing member and loan information.
        """
        book = self.get_book_by_name(book_name)
        if not book:
            logger.warning(f"No book found with title '{book_name}'.")
            return []

        ### YOUR QUERY ###
        # query = ...
        # params = ...
        # remove the following line after your implementation



        query = """
        SELECT member.id, member.name 
        FROM member
        JOIN loan ON member.id = loan.member_id
        WHERE loan.book_id = %s;
        """


        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (book.id,))
        members = cursor.fetchall()

        cursor.close()
        conn.close()

        try:
            return self.db.fetch_results(query = query, params = params)
        except Exception as e:
            logger.error(f"Failed to fetch members for book '{book_name}': {e}")
            return []

    def get_all_loans(self) -> List[tuple]:
        """
        Fetches all loans from the database.

        Returns:
            List[tuple]: A list of tuples containing loan information.
        """
        ### YOUR QUERY ###
        # query = ...
        # remove the following line after your implementation
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM loan;"

        cursor.execute(query)
        loans = cursor.fetchall()

        cursor.close()
        conn.close()

        try:
            return self.db.fetch_results(query = query)
        except Exception as e:
            logger.error(f"Failed to fetch loans: {e}")
            return []
