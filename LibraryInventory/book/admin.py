from django.contrib import admin
from book.models import Book, Author, Genre, Language, Publisher


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    search_fields = ['isbn10', 'isbn13', 'title', 'authors__first_name', 'authors__last_name']
    autocomplete_fields = ['authors', 'language', 'genre', 'publisher']
    list_display = ['title', 'get_authors_string', 'publisher', 'release_date', 'language']
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
    ]


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']


class GenreAdmin(admin.ModelAdmin):
    search_fields = ['id']


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name']


class LanguageAdmin(admin.ModelAdmin):
    search_fields = ['id']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Language, LanguageAdmin)
