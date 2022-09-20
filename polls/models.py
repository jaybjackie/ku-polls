import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date end', null=True)

    def __str__(self):
        return self.question_text
    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def is_published(self):
        return (timezone.now() >= self.pub_date)
        
    def can_vote(self):
        time = timezone.now()
        if self.is_published():
            # Question had published
            if self.end_date is None:
                # Null end date
                return True
            else:
                return (time <= self.end_date)
        else:
            return False

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    
    @property
    def votes(self):
        """Count the vote that refer to this choice."""
        count = Vote.objects.filter(choice=self).count()
        return count

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.choice}"