from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from post.models import Post


class IndexView(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.all()
    template_name = 'index.html'
