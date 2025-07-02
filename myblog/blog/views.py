from django.views.generic import ListView, DetailView
from .models import Post

class PostListView(ListView):
    queryset = Post.objects.filter(published=True).order_by('-created_at')
    paginate_by = 6
    template_name = 'blog/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'slug'