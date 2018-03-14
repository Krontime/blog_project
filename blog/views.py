from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import NewPostForm, Post

def post_list(request):
    return render(request, 'blog/post_list.html')


def post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/post_details.html', {'post': post})


def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        message = form.save(commit=False)
        
        # message.sender = request.user
        message.save()
        return redirect('post_list')
    else:
        form = NewPostForm()
    
    return render(request, "blog/new_post.html", {'form': form})
