from flask import Flask, Blueprint, render_template, request, redirect, url_for
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

books_blueprint = Blueprint("books", __name__)


@books_blueprint.route("/")
def home():
    return render_template("index.html")


@books_blueprint.route("/books")
def show_books():
    books = book_repository.select_all_books()
    return render_template("show.html", books=books)
