from django.views import View
from django.shortcuts import render
from book.utils import FormException


class ContactView(View):
    def get(self, request):
        return render(request, 'book/contact.html')

    def post(self, request):
        try:
            resp = request.POST
            first_name = resp.get("myFName")
            last_name = resp.get("myLName")
            print(first_name)
            if not first_name.isalpha():
                raise FormException({"error": "Invalid First Name."})
            if not last_name.isalpha():
                raise FormException({"error": "Invalid Last Name"})
            return render(request, 'book/thanks.html')
        except FormException as error:
            print(error.args[0])
            return render(request, 'book/contact.html', {'input_error': error.args[0]["error"]})


