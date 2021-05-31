import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


# Definitions of data models.
# Each model subclasses the django.db.models.Model class.
# manage.py makemigrations polls >> update these models
# table names generated as "app_model" (polls_question)

class Question(models.Model):
    # Each field is an instance of the Field class.
    question_text = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')

    # str() methods make db more readable
    def __str__(self):
        return self.question_text

    # from django.contrib, prettifies display for arbitrary method
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    # associates each Choice to a Question
    # each such question is given a choice_set field (see RelatedManager)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
