from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import NewPostForm
from django.utils import timezone

def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {'posts': posts})


def post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()
    return render(request, "blog/post_details.html", {'post': post})


def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("view_post", post.pk)
    else:
        form = NewPostForm()
    
    return render(request, "blog/new_post.html", {'form': form})

def edit_post(request, id):
    item = get_object_or_404(Post, pk=id)
    
    if request.method == "POST":
        print("POST")
        form = NewPostForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("view_post", id)
    else:
        print("GET")
    
    form = NewPostForm(instance = item)
    return render(request, "blog/edit_post.html", {'form': form,})

def delete_post(request, id):
    item = get_object_or_404(Post, pk=id)
    item.delete()
    return redirect("home")