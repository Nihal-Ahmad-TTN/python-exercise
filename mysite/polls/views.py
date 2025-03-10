from django.db.models import F
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import permission_required
from .models import Choice, Question, ChoiceForm

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]
    

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})


# def feedback_view(request):
#     if request.method == "POST":
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             # Process data
#             name = form.cleaned_data['question']
#             email = form.cleaned_data['choice_text']
#             # feedback = form.cleaned_data['feedback']
#             print(f"Received feedback from {name}: {email}")
#             return redirect('index.html')
#     else:
#         form = QuestionForm()
    
#     return render(request, 'index.html')

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    

class FormView(generic.FormView):
    template_name = "polls/detail.html"
    form_class = ChoiceForm
    success_url = "polls/results.html"
    def form_valid(self, form):
        form
        return super().form_valid(form)
    

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def voteform(request, question_id):
    form = ChoiceForm(request.POST)
    if form.is_valid():
        vote = form.cleaned_data['choice_text']
        form.save()
        return HttpResponse(f"you voted for {vote}")
    else:
        form = ChoiceForm()
    return render(request, "polls/detail.html", {'form' : form})

@permission_required('view_result')
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
    

