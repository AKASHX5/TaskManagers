from django.urls import path

from .views import TaskView


app_name = "task"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('task/', TaskView.as_view()),
]

