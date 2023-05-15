# urls.py
from django.urls import path
from post.views import IndexView

urlpatterns = [
    path("", IndexView.as_view()),
]
