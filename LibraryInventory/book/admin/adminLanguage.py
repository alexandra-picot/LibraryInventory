from django.contrib import admin
from book.models import Language


# For more information about all the attributes into the Admin models, refer to the Django documentation
# https://docs.djangoproject.com/en/2.2/ref/contrib/admin/#modeladmin-options


class LanguageAdmin(admin.ModelAdmin):
    """
    Language admin model, it is link to the Language model

    This model correspond to what will be shown in the admin interface when a editing/adding books and in the book
    listing
    """

    # Fields that can be searched in the search bar on the book listing page
    search_fields = ['id']

    # Disable the possibility to go in the detail view
    list_display_links = None

    ordering = ['id']

    def has_delete_permission(self, request, obj=None):
        """
        Remove the permission to delete a language for ALL the users

        :param request: Unused
        :param obj: Unused
        :return: False, the permission
        """
        return False

    def has_add_permission(self, request):
        """
        Remove the permission to add a new language for ALL the users

        :param request: Unused
        :param obj: Unused
        :return: False, the permission
        """
        return False

    def has_change_permission(self, request, obj=None):
        """
        Remove the permission to change/edit a language for ALL the users

        :param request: Unused
        :param obj: Unused
        :return: False, the permission
        """
        return False


# Register the model to be shown in the admin interface
admin.site.register(Language, LanguageAdmin)
