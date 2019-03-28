from django.contrib import admin
from book.models import Book, Transaction


# For more information about all the attributes into the Admin models, refer to the Django documentation
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#modeladmin-options


class TransactionInLine(admin.TabularInline):
    """
    Transaction admin model for Inline use, is used in BookAdmin class

    This model correspond to what will be shown in the admin interface when a editing/adding books in the inline section
    """

    # Model on which this admin class is based
    model = Transaction

    # Show one new row to add after the list of transactions
    extra = 1

    # Order the inline transactions by date descending order
    ordering = ('-date',)

    def has_change_permission(self, request, obj=None):
        """
        Set the permission to change/edit the inline transactions to false

        :param request: Unused
        :param obj: Unused
        :return: False, the permission
        """
        return False


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

    inlines = [TransactionInLine]

    # def get_formsets_with_inlines(self, request, obj=None):
    #     for line in self.get_inline_instances(request, obj):
    #         print(line.model.type)
    #         yield line.get_formset(request, obj), line
    #
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "transaction":
    #         kwargs["queryset"] = Transaction.objects.all().order_by('date')
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        self.readonly_fields = ['isbn10', 'isbn13', 'authors', 'language', 'release_date', 'title', 'publisher']
        return super().change_view(
            request, object_id, form_url
        )


# Register the model to be shown in the admin interface
admin.site.register(Book, BookAdmin)
