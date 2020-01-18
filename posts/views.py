from django.shortcuts import render, get_object_or_404,redirect
from django.contrib import messages
from .models import Post, Author
from .forms import PostModelForm


# Create your views here.
def posts_list(request):
    all_posts = Post.objects.all()
    context = {
        'all_posts': all_posts,
    }
    return render(request, 'posts/posts_list.html', context)


def posts_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'posts/posts_detail.html', context)


def posts_create(request):
    author = Author.objects.get(user=request.user)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = author
            form.save()
            messages.success(request, "Post Created")

            return redirect('/posts/')
    else:
        form = PostModelForm()

    context = {
        'form': form,
        'type': 'Create',
    }
    return render(request, 'posts/posts_form.html', context)


def posts_update(request, slug):
    post_to_update = get_object_or_404(Post, slug=slug)
    author = Author.objects.get(user=request.user)
    if request.method == 'POST':
        form = PostModelForm(request.POST, request.FILES, instance=post_to_update)
        if form.is_valid():
            form.instance.author = author
            form.save()
            messages.success(request, "Post Updated")
            return redirect('/posts/')
    else:
        form = PostModelForm(instance=post_to_update)

    context = {
        'form': form,
        'type': 'Update'
    }
    return render(request, 'posts/posts_form.html', context)


def posts_delete(request, slug):
    post_to_delete = get_object_or_404(Post, slug=slug)
    messages.success(request, "Post Deleted")
    post_to_delete.delete()
    return redirect('/posts/')
