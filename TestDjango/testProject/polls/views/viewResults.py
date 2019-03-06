from django.views import generic
from polls.models import Question


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'