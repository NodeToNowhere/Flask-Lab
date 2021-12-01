import pdb

from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all_books()
author_repository.delete_all_authors() #ask why this doesnt work other wya

author1 = Author("Banks")
author_repository.save_author(author1)
author2 = Author("Pratchet")
author_repository.save_author(author2)

book1 = Book("Madness", 9872, author1)
book_repository.save_book(book1)
book2 = Book("Calm", 3, author2)
book_repository.save_book(book2)
