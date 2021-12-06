from django.shortcuts import render
from blog.models import Post


# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})


def sobre(request):
    return render(request, 'about.html')


def contato(request):
    return render(request, 'contact.html')
