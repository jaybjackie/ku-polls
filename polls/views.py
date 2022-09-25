from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from .models import Choice, Question, Vote
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    """Class based view for viewing a poll."""
    model = Question
    template_name = 'polls/detail.html'
    # check for end_date question, if end then return to index page
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
        

    def get(self, request, **kwargs):
        """
         If question doesn't exist or closed, redirect to index page.
         Stores previous vote of voted question.
         """
         # get question
        question = get_object_or_404(Question, pk=kwargs['pk'])
        try: # try get the previous vote
            vote = Vote.objects.get(user=request.user, choice__in=question.choice_set.all())
            previous_vote = vote.choice
        except Vote.DoesNotExist: # except vote not found then previous vote is empty
            previous_vote = ''
        if not question.can_vote(): # if have not validate to vote, return to index instead
            response = redirect('polls:index')
            response.status_code = 404
            return response
        # can vote, go for vote and provide the previous_vote; either choice or empty
        return render(request, 'polls/detail.html', {'question': question, 'previous_vote':previous_vote})
   
            
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


@login_required
def vote(request, question_id):
    """Vote for a choice on a question (poll)."""
    user = request.user
    question = get_object_or_404(Question, pk=question_id)

    if not user.is_authenticated: # if not authenticated return to login page
        return redirect('login')
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        has_voted = Vote.objects.filter(choice__question=question, user=user)
        if has_voted: # already vote
            old_vote = has_voted[0]
            if old_vote != selected_choice: # vote on new choice
                old_vote.delete() 
        new_vote = Vote(user=user, choice=selected_choice)
        new_vote.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def signup(request):
    """Register a new user."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passwd = form.cleaned_data.get('passwd')
            user = authenticate(username=username, password=raw_passwd)
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('polls:index')
        else:
            # django handle the existing user.
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})