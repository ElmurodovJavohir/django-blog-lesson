
# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView
from post.models import Post


class IndexView(ListView):
    model = Post
    context_object_name = 'post_list'
    queryset = Post.objects.all()
    template_name = 'index.html'
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'
