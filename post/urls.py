# urls.py
from django.urls import path
from post.views import IndexView, PostDetailView

urlpatterns = [
    path("", IndexView.as_view()),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
