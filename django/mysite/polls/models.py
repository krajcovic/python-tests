import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Question(models.Model):
    """
    Class contains questions.
    """

    question_text = models.CharField(max_length=200)
    """Question text."""

    pub_date = models.DateTimeField('date published')
    """Date of published."""

    def __str__(self):
        return '{}'.format(self.question_text, self.pub_date)

    def was_published_recently(self):
        """
        Return True for recently published questions
        :return: True/False
        """
        now = timezone.now()
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    """Class of choices."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Poll(models.Model):
    pass


class Reporter(models.Model):
    pass


class Article(models.Model):
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)


class Topping(models.Model):
    pass


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
