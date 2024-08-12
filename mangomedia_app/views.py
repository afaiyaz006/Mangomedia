from django.shortcuts import render
from .forms import MangoPostForm
# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        form = MangoPostForm(request.POST)
        if form.is_valid():
   
            mangopost=form.save(commit=False)
            mangopost.author = request.user
            mangopost.save()
            form = MangoPostForm()
    else:
        form = MangoPostForm()
            
    return render(request,'mangomedia_app/index.html',{"mango_form":form})
    

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

