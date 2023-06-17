from django.http import HttpResponse
from .models import Question
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_question_list = Question.objects.all()
    return render(request, "polls/index.html",{
        "latest_question_list" : latest_question_list
        })



# Create your views here.

def detail(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request, "polls/detail.html",{
        "question" : question
        })



def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta {question_id}")


def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta numero: {question_id}")
