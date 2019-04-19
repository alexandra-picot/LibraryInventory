from django.views import View
from django.shortcuts import render


class ThanksView(View):
    def get(self,request):
        return render(request,'book/thanks.html')
    def post(self,request):
        return render(request,'book/thanks.html')

