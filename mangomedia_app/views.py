from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request,'mangomedia_app/index.html')

def profile(request):
    return render(request,'accounts/profile.html')

def dummy(request):
    return render(request,'mangomedia_app/dummy.html')

def create_post(request):
    
    return render(request,'mangomedia_app/create_post.html')