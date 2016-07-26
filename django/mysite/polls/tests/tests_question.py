#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime

from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class TestQuestion(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently(should return False for questions whose pub_date is in the future.
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recentrly() should return False for questions whose pub_date is older than 1 day.
        :return:
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)