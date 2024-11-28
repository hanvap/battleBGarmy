from django.shortcuts import render

# social_share/views.py

from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy

from .forms import PostForm
from .models import Post

def post_detail(request,):
    post = Post.objects.last()
    context = {
        'post': post,
    }
    return render(request, 'posts/post.html', context)

class PostCreateView(CreateView):
    model = Post
    template_name = "posts/post_create.html"
    form_class = PostForm
    success_url = reverse_lazy('post_detail')