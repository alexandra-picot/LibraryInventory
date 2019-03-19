from django.test import TestCase
from book.models import Book, Author, Genre, Language, Publisher
from .utils import *


class BookModelTests(TestCase):

    def test_get_authors_string_without_authors(self):
        book_no_author = create_test_book()
        self.assertEqual("", book_no_author.get_authors_string())

    def test_get_authors_string_with_one_author(self):
        author = create_test_author()
        book_one_author = create_test_book()
        book_one_author.authors.add(author)
        self.assertEqual("Foo Bar", book_one_author.get_authors_string())

    def test_get_authors_string_with_two_authors(self):
        author = create_test_author()
        author2 = Author(pk=2, first_name="Moo", last_name="Toto")
        author2.save()
        book_two_authors = create_test_book()
        book_two_authors.authors.add(author, author2)
        self.assertEqual("Foo Bar, Moo Toto", book_two_authors.get_authors_string())