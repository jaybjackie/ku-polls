import datetime
from polls.models import Vote, Question
from django.utils import timezone
from django.contrib.auth.models import User
from django.test import TestCase


def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

def create_user(username, raw_passwd):
    user = User.objects.create_user(username=username, password= raw_passwd)
    user.save()
    return user

def create_choice(question, choice_text):
    choice = question.choice_set.create(choice_text=choice_text)
    return choice


class QuestionVoteTests(TestCase):
    def test_confirm_vote(self):
        user = create_user('Jason', 'JasonSoCool')
        voted_question = create_question(question_text='Demo Question', days=0)
        select_choice = create_choice(voted_question, choice_text="some options")
        
        old_vote = Vote(user=user, choice=select_choice)
        self.assertEqual(select_choice.votes, 0)
        old_vote.save()
        self.assertEqual(select_choice.votes, 1)
