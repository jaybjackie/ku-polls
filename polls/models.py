import datetime
from time import time
from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create Models here

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
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
