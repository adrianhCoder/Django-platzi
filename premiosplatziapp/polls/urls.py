from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name=""),
    # ex: /polls/18
    path("<int:question_id>/", views.detail, name=""),
    # ex: /polls/18/results
    path("<int:question_id>/results", views.results, name=""),
    # ex: /polls/18/vote
    path("<int:question_id>/vote", views.vote, name="")

]
