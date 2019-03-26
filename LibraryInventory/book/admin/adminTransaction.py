from django.contrib import admin
from book.models import Transaction


# For more information about all the attributes into the Admin models, refer to the Django documentation
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#modeladmin-options


class TransactionAdmin(admin.ModelAdmin):
    """
       Transaction admin model, it is link to the Transaction model

       This model correspond to what will be shown in the admin interface when a editing/adding books and in the book
       listing
       """

    # Fields to display when on the book listing page
    list_display = ['book', 'type', 'book_state', 'quantity', 'date']

    # # Replace given standard dropdown (select box) fields into autocomplete field for easier use
    autocomplete_fields = ['book']

    # # Fields that can be searched in the search bar on the book listing page
    search_fields = ['book']

    list_display_links = None


# Register the model to be shown in the admin interface
admin.site.register(Transaction, TransactionAdmin)