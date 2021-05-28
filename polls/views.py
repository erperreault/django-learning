from django.urls import reverse
from django.http import HttpResponseRedirect

# render fills in for HttpRequest and template.loader
from django.shortcuts import render, get_object_or_404

# templates for the common stuff
from django.views import generic

# our own data models
from .models import Choice, Question


class IndexView(generic.ListView):
    # ListView is a generic view from django.views
    template_name = 'polls/index.html'

    # context is normally automatic but can be overridden
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # DetailView is another generic view from django.views
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    # get the desired question by id
    question = get_object_or_404(Question, pk=question_id)

    try:
        # request.POST works like a dict, look-up by key name
        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()

        # always return Redirect on successful handling, to prevent
        # double-submission.
        # reverse() returns something like '/polls/3/results/' 
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
