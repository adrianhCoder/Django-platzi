from django.db import models
from django.utils import timezone
import datetime

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def save(self, *args, **kwargs):
        ##super().save(*args, **kwargs)
        is_added_from_admin = models.BooleanField(default=False)
        if(is_added_from_admin):
            print("HELL YHEA")
            #### Here is the juice!
        choices = kwargs.get("choices")  # retrieve al questions

        if choices and len(choices) > 0:
            kwargs.pop("choices", None)
            super().save(*args, **kwargs)  # If choices > 0 save question

            for choice in choices:  # Iterate trough all choices
                choice.question = self  # Asign choice to the questions
                choice.save()  # Save it
        else:
            raise ValueError("Should have choices")

        

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return (
            timezone.now()
            >= self.pub_date
            >= timezone.now() - datetime.timedelta(days=1)
        )



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
