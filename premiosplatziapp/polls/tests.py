import datetime

from .models import Question

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

# Create your tests here.


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """Was published recentlly returns
        false for questions whos pub date is in the fytyre"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Helloy", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_in_the_past(self):
        """Checks if an answer was published in the past"""
        time = timezone.now() - datetime.timedelta(days=30)
        past_question = Question(question_text="Question text here", pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)

    def test_was_published_recently_to_timenow_questions(self):
        """Checks if question created now is recent"""
        time = timezone.now()
        now_question = Question(question_text="Question text here", pub_date=time)
        self.assertIs(now_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If there is no questions , an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
