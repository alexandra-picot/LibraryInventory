from django.views import View
from django.shortcuts import render
from book.utils import FormException

class ThanksView(View):
    def get(self,request):
        return render(request,'book/thanks.html')
    def post(self,request):
        return render(request,'book/thanks.html')

#try:
    #raise FormException({"input_error": "Invalid First Name.","input_error": "Invalid Last Name"})
#except FormException as error:
    #myFName = error.args[0]
    #myLname = error.args[1]
    #print(myFName["input_error"])
    #print(myLName["input_error"])