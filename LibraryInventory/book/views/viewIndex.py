from django.views import generic


class IndexView(generic.TemplateView):
    template_name = 'book/index.html'
