from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("You are in the main page of premiosplatziapp")


# Create your views here.

def detail(request, question_id):
    return HttpResponse(f"Estas viendo la pregunta numero {question_id}")


def results(request, question_id):
    return HttpResponse(f"Estas viendo los resultados de la pregunta {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Estas votando a la pregunta numero: {question_id}")

