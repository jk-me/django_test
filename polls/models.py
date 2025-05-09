import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
# models build on subclasses of models import

# question_text and pub_date for ex. will be column names
# Field classes for data type, ForeignKey class for relationships

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now)

    def __str__(self):
        return self.question_text

    @admin.display(
      boolean=True,
      ordering="pub_date", #define a sorting order for this method
      description="Published recently?",
    )
    def was_published_recently(self):
      now = timezone.now()
      # pub date was in the last day (published after or at current time - 1 day)
      return now >= self.pub_date >= now - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text