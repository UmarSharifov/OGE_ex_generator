from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Model_Word(models.Model):
    word = models.CharField(max_length=100)
    def __str__(self):
        return str(self.word)


class Results(models.Model):
    Owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='Owner')
    Correct_answers = models.IntegerField()
    Answers_quantity = models.IntegerField()
    Lvl = models.IntegerField(null=True, blank=True)
    Pass_date = models.DateTimeField(default=timezone.now)


