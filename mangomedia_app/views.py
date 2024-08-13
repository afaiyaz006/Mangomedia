from django.shortcuts import render
from mangomedia_app.forms import MangoPostForm
from mangomedia_app.models import MangoPost
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse


def index(request):
    mangoposts=None
    form=None
    
    if request.user.is_authenticated:
        mangoposts = MangoPost.objects.all().order_by('-author')
        mangoposts_paginated = Paginator(mangoposts,1)
        
        page_number = request.GET.get("page")
        mangoposts = mangoposts_paginated.get_page(page_number)
        if request.method == "POST":
            form = MangoPostForm(request.POST)
            if form.is_valid():
                find_user_obj = User.objects.get(username=request.user)
                mangopost=form.save(commit=False)
                
                mangopost.save()
                mangopost.author.add(find_user_obj)
                form = MangoPostForm()
        else:
            form = MangoPostForm()
            
    return render(request,'mangomedia_app/index.html',{"mango_form":form,'mangoposts':mangoposts})
    

def profile(request):
    return render(request,'accounts/profile.html')

def dummy(request):
    return render(request,'mangomedia_app/dummy.html')

def create_post(request):
    
    if request.method == "POST":
        form = MangoPostForm(request.POST)
        if form.is_valid():
            print(form)
    else:
        form = MangoPostForm()
            
    return render(request,'mangomedia_app/create_post.html',{"mango_form":form})

def mango_posts(request):
    mangoposts=None
    if request.method=="GET":
        mangoposts = MangoPost.objects.all().order_by('-author')
       
        mangoposts_paginated = Paginator(mangoposts,1)
      
        page_number = request.GET.get("page")
        mangoposts = mangoposts_paginated.get_page(page_number)
    return render(request,'mangomedia_app/mangoposts_list.html',{'mangoposts':mangoposts})
        