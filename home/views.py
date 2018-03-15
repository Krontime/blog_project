from django.shortcuts import render
from blog.models import Post

def get_home_index(request):
    posts = Post.objects.all()
    return render(request, 'home/index.html', {'posts': posts})
