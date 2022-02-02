import imp
from django.shortcuts import redirect, render 
from .forms import *
from home.models import *


def home(request):
    return render(request , 'home.html')    


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request , 'register.html')    

def add_blog(request):

    context = {'form':BlogForm}
    try:
        if request.method == 'POST':
           
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            if form.is_valid():
                content = form.cleaned_data['content']
            blog_obj = BlogModel.objects.create(
                user = user ,
                title = title,
                content = content,
                image = image
            )    
            return redirect('/add-blog/')

    except Exception as e:

        print('Exception :', e)


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