import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase

# Create your tests here.
from django.utils import timezone

from polls.models import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class TestsQuestionView(TestCase):
    def test_index_view_with_no_questions(self):
        """
        If no question exist, an appropriate message shold be dispalyed.
        :return:
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the index page
        :return:
        """
        create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'], ['<Question: Past question.>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: Past question.>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question(question_text='Past question 1.', days=-30)
        create_question(question_text='Past question 2.', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'], ['<Question: Past question 2.>', '<Question: Past question 1.>']
        )


class TestsQuestionIndexDetail(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of question with a pub_date in the future should return a 404 not found.
        :return:
        """
        future_question = create_question(question_text='Future question', days=5)
        response = self.client.get(reverse('polls:detail', args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of question with a pub_date in the past should display the questio's text.
        :return:
        """

        past_question = create_question('Past Question.', -5)
        response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)
