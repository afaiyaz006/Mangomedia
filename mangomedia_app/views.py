from django.shortcuts import render, redirect, get_object_or_404
from mangomedia_app.forms import MangoPostForm, CommentForm
from mangomedia_app.models import MangoPost, Comment
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator

def index(request):
    mangoposts = None
    form = None
    comment_form = CommentForm()
    
    if request.user.is_authenticated:
        mangoposts = MangoPost.objects.all().order_by('-created_at')
        mangoposts_paginated = Paginator(mangoposts, 5)  
        
        page_number = request.GET.get("page",1)
        mangoposts = mangoposts_paginated.get_page(page_number)
        
        if request.method == "POST":
            form = MangoPostForm(request.POST)
            if form.is_valid():
                mangopost = form.save(commit=False)
                mangopost.save()
                mangopost.author.add(request.user)
                form = MangoPostForm()
        else:
            form = MangoPostForm()
            
    return render(request, 'mangomedia_app/index.html', {
        "mango_form": form,
        'mangoposts': mangoposts,
        'comment_form': comment_form
    })

@login_required
def like_post(request, post_id):
    post = get_object_or_404(MangoPost, id=post_id)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return render(request, 'mangomedia_app/partials/like_button.html', {'post': post})

@login_required
def add_comment(request, post_id):
    post = get_object_or_404(MangoPost, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    
    # Fetch all comments for the post
    comments = post.comments.all().order_by('-created_at')
    
    return render(request, 'mangomedia_app/partials/comments_section.html', {
        'post': post,
        'comments': comments,
        'comment_form': CommentForm()
    })
    
def profile(request):
    return render(request, 'accounts/profile.html')

def dummy(request):
    return render(request, 'mangomedia_app/dummy.html')

def create_post(request):
    if request.method == "POST":
        form = MangoPostForm(request.POST)
        if form.is_valid():
            mangopost = form.save(commit=False)
            mangopost.save()
            mangopost.author.add(request.user)
            return redirect('index')
    else:
        form = MangoPostForm()
            
    return render(request, 'mangomedia_app/create_post.html', {"mango_form": form})

def mango_posts(request):
    mangoposts = None
    if request.method == "GET":
        mangoposts = MangoPost.objects.all().order_by('-created_at')
        mangoposts_paginated = Paginator(mangoposts, 10)  # Changed to 10 posts per page
        page_number = request.GET.get("page")
        mangoposts = mangoposts_paginated.get_page(page_number)
    return render(request, 'mangomedia_app/mangoposts_list.html', {'mangoposts': mangoposts})



from django.core.paginator import Paginator
from django.shortcuts import render

# ... existing imports and views ...

def load_more_posts(request):
    page_number = request.GET.get('page', 1)
   
    all_posts = MangoPost.objects.all().order_by('-created_at')
    paginator = Paginator(all_posts, 5)  # 5 items per page
    mangoposts = paginator.get_page(page_number)
    
    return render(request, 'mangomedia_app/partials/post_list.html', {'mangoposts': mangoposts})