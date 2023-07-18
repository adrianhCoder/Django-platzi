import datetime

from .models import Question

from django.test import TestCase
from django.utils import timezone

# Create your tests here.

class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """Was published recentlly returns
        false for questions whos pub date is in the fytyre"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text='Helloy',pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
        