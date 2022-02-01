from django.shortcuts import render 
from .forms import *


def home(request):
    return render(request , 'home.html')    


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request , 'register.html')    

def add_blog(request):

    context = {'form':BlogForm}
    return render(request , 'add_blog.html' , context)

def blog_detail(request):
    return render(request , 'base_details.html')

def see_blog(request):
    return render(request , 'see_blog.html')

def blog_delete(request):
    pass

def blog_update(request):
   return render(request , 'update_blog.html')


def logout_view(request):
    pass

def verify(request):
    pass