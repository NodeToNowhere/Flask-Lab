from db.run_sql import run_sql

from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository


def save_book(book):
    sql = "INSERT INTO books (title, pages, author_id) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.pages, book.author.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    book.id = id
    return book


def select_all_books():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select_author(row["author_id"])
        book = Book(row["title"], row["pages"], author, row["id"])
        books.append(book)
    return books


def delete_all_books():
    sql = "DELETE  FROM books"
    run_sql(sql)
