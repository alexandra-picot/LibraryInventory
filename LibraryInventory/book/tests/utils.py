from book.models import Book, Author, Genre, Language, Publisher


def create_test_author():
    author = Author(pk=1, first_name="Foo", last_name="Bar")
    author.save()
    return author


def create_test_genre():
    genre = Genre(pk="Fantasy")
    genre.save()
    return genre


def create_test_language():
    language = Language(pk="French")
    language.save()
    return language


def create_test_publisher():
    publisher = Publisher(pk=1, name="LaFonte")
    publisher.save()
    return publisher


def create_test_book():
    genre = create_test_genre()
    language = create_test_language()
    publisher = create_test_publisher()
    book = Book(pk=1, isbn10=0000000000, title="Foo", description="Foo foo foo",
                genre=genre, language=language,
                release_date="1995-01-01", publisher=publisher, price_new=10)
    book.save()
    return book