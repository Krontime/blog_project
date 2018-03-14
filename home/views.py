from django.shortcuts import render
from blog.models import Post

def get_home_index(request):
    post = Post.objects.all()
    return render(request, 'home/index.html', {'post': post})