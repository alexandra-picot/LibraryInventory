from typing import List, Dict, Tuple
from django.contrib import admin
from book.models import Book, Author, Genre, Language, Publisher, Transaction

# For more information about all the attributes into the Admin models, refer to the Django documentation
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#modeladmin-options


class BookAdmin(admin.ModelAdmin):
    """
    Book admin model, it is link to the Book model

    This model correspond to what will be shown in the admin interface when a editing/adding books and in the book
    listing
    """

    # Fields that can be searched in the search bar on the book listing page
    search_fields = ['isbn10', 'isbn13', 'title', 'authors__first_name', 'authors__last_name']

    # Replace given standard dropdown (select box) fields into autocomplete field for easier use
    autocomplete_fields = ['authors', 'language', 'genre', 'publisher']

    # Fields to display when on the book listing page
    list_display = ['title', 'get_authors_string', 'publisher', 'release_date', 'language']

    # Make sections into the add/edition page of a book so that it's clearer
    # This is a list containing tuples (One tuple == One section)
    # Each tuples contains a string (the name of the section to display) and a dict
    # The dict has for key the string 'fields' (enforced by Django)
    # and a list containing the names of all the attributes in the section
    fieldsets = [
        (
            'General Information', {'fields': ['isbn10', 'isbn13',
                                               'title', 'description',
                                               'authors', 'genre',
                                               'release_date', 'publisher',
                                               'language']}
        ),
        (
            'Prices', {'fields': ['price_new', 'price_used', 'price_ebook',
                                  'rent_new', 'rent_used', 'rent_ebook']}
        ),
    ]  # type: List[ Tuple[str, Dict[str, List[str] ] ] ]

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.readonly_fields = ['isbn10', 'isbn13', 'authors', 'language', 'release_date', 'title', 'publisher']
        return super().change_view(
            request, object_id, form_url
        )


class AuthorAdmin(admin.ModelAdmin):
    """
    Author admin model, it is link to the Author model

    This model correspond to what will be shown in the admin interface when a editing/adding books and in the book
    listing
    """

    # Fields that can be searched in the search bar on the book listing page
    search_fields = ['first_name', 'last_name']


class GenreAdmin(admin.ModelAdmin):
    """
    Genre admin model, it is link to the Genre model

    This model correspond to what will be shown in the admin interface when a editing/adding books and in the book
    listing
    """

    # Fields that can be searched in the search bar on the book listing page
    search_fields = ['id']


class PublisherAdmin(admin.ModelAdmin):
    """
    Publisher admin model, it is link to the Publisher model

    This model correspond to what will be shown in the admin interface when a editing/adding books and in the book
    listing
    """

    # Fields that can be searched in the search bar on the book listing page
    search_fields = ['name']


class LanguageAdmin(admin.ModelAdmin):
    """
    Language admin model, it is link to the Language model

    This model correspond to what will be shown in the admin interface when a editing/adding books and in the book
    listing
    """

    # Fields that can be searched in the search bar on the book listing page
    search_fields = ['id']


class TransactionAdmin(admin.ModelAdmin):
    """
       Transaction admin model, it is link to the Transaction model

       This model correspond to what will be shown in the admin interface when a editing/adding books and in the book
       listing
       """

    # Fields to display when on the book listing page
    list_display = ['book', 'type', 'book_state', 'quantity']

    # # Replace given standard dropdown (select box) fields into autocomplete field for easier use
    autocomplete_fields = ['book']

    # # Fields that can be searched in the search bar on the book listing page
    search_fields = ['book']


# Register the models to be shown in the admin interface
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Transaction, TransactionAdmin)
