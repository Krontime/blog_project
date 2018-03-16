from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import NewPostForm
from django.utils import timezone
from django.http import HttpResponseForbidden

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-published_date')
    return render(request, "blog/post_list.html", {'posts': posts})
    
    
def post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views += 1
    post.save()

    can_edit = post.can_be_edited_by(request.user)

    return render(request, "blog/post_detail.html", {'post': post, 'can_edit': can_edit})


def new_post(request):
    
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    
    if request.method=="POST":
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_list")
    else:
        form = NewPostForm()
    
    return render(request, "blog/post_form.html", { 'form': form })


def edit_post(request, id):
   post = get_object_or_404(Post, pk=id)
   
   if post.can_be_edited_by(request.user):
       return HttpResponseForbidden()
   
   if request.method == "POST":
       form = NewPostForm(request.POST, request.FILES, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect(post_details, post.pk)
   else:
       form = NewPostForm(instance=post)
   return render(request, 'blog/post_form.html', {'form': form})
  
def delete_post(request, id):
    item = get_object_or_404(Post, pk=id)
    item.delete()
    return redirect("home")
