"""Test for Question Models with time."""
import datetime
from django.test import TestCase
from django.utils import timezone
from polls.models import Question

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
    
    def test_question_no_end(self):
        pubed_time = timezone.now() - datetime.timedelta(hours=1)
        waiting_time = timezone.now() + datetime.timedelta(hours=1)
        published_question = Question(pub_date=pubed_time)
        waiting_question = Question(pub_date=waiting_time)
        self.assertIs(published_question.is_published(), True)
        self.assertIs(waiting_question.is_published(), False)

    def test_publised_can_vote(self):
        before_end = timezone.now() + datetime.timedelta(hours=2)
        pub_time = timezone.now() - datetime.timedelta(hours=5)
        after_end = timezone.now() - datetime.timedelta(hours=2)
        must_valid = Question(pub_date=pub_time, end_date= before_end)
        must_invalid = Question(pub_date=pub_time, end_date=after_end)
        null_end = Question(pub_date=pub_time)
        self.assertIs(null_end.can_vote(), True)
        self.assertIs(must_valid.can_vote(), True)
        self.assertIs(must_invalid.can_vote(), False)

    def test_future_vote(self):
        time = timezone.now() + datetime.timedelta(hours=10)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.can_vote(), False)
    
    def test_exact_pub_time(self):
        time = timezone.now()
        exact_pub = Question(pub_date=time)
        self.assertIs(exact_pub.can_vote(), True)

    def test_late_vote(self):
        pub_time = timezone.now() - datetime.timedelta(hours=2)
        end_time = timezone.now() - datetime.timedelta(hours=1)
        new_question = Question(pub_date=pub_time, end_date=end_time)
        self.assertIs(new_question.can_vote(), False)
