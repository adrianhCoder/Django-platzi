from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/18
    path("<int:pk>/detail/cambiandotodoojaja", views.DetailView.as_view(), name="detail"),
    # ex: /polls/18/results
    path("<int:pk>/results", views.ResultView.as_view(), name="results"),
    # ex: /polls/18/vote
    path("<int:pk>/vote", views.vote, name="vote")

]
