import datetime

from .models import Question, Choice

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone

# Create your tests here.


def Create_Question(text, date):
    question_created = Question(question_text=text, pub_date=date)

    choice1 = Choice(choice_text="Choice 1", question=question_created, votes=1)
    choice2 = Choice(choice_text="Choice 2", question=question_created, votes=1)
    choice3 = Choice(choice_text="Choice 3", question=question_created, votes=1)

    question_created.save(choices=(choice1, choice2, choice3))
    return question_created


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """Was published recentlly returns false for questions whos pub date is in the fytyre"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Create_Question("Helloy", time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_in_the_past(self):
        """Checks if an answer was published in the past"""
        time = timezone.now() - datetime.timedelta(days=30)
        past_question = Create_Question("Question text here", time)
        self.assertIs(past_question.was_published_recently(), False)

    def test_was_published_recently_to_timenow_questions(self):
        """Checks if question created now is recent"""
        time = timezone.now()
        now_question = Create_Question("Question text here", time)
        self.assertIs(now_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If there is no questions , an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_no_future_questions_showed(self):
        """Checks if a future question is showed in the index"""
        present_question = Create_Question("Present Question", timezone.now())
        future_question = Create_Question(
            "Future Question", timezone.now() + datetime.timedelta(days=30)
        )

        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Present Question")
        self.assertNotContains(response, "Future Question")


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """If question id not exists, get 404"""
        question = Create_Question(
            "Future Question", timezone.now() + datetime.timedelta(days=30)
        )

        url = reverse("polls:detail", args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """Checks if past questions are url avaiable"""
        question = Create_Question(
            "Future Question", timezone.now() - datetime.timedelta(days=30)
        )

        url = reverse("polls:detail", args=(question.id,))
        response = self.client.get(url)
        self.assertContains(response, question.question_text)
