from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import Post, Comment
from .forms import PostForm, CommentForm

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-timestamp'[:50])
    template_name = "home_index.html"
    paginate_by = 3
    
    
def PostDetail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect('post-detail', slug=slug)
    else:
        form = CommentForm()
        
    context = {
        'post':post, 'comments':comments, 'form': form, 
        'new_comment':new_comment
    }
    return render(request, 'post_details.html', context)

@login_required
def create_post(request):
    owner = request.user
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = owner
            new_topic.save()
            return redirect('home-index')
    else:
        form = PostForm()
        
    context = {
        'form': form
    }
    return render(request, 'create_post.html', context)

@login_required
def edit_post(request, slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = PostForm(instance=post, data=request.POST)
        form.save()
        return redirect('post-detail', slug=slug)
    else:
        form = PostForm(instance=post)
        
    context = {
        'form': form
    }
    return render(request, 'edit_post.html', context)