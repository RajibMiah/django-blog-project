
from django.shortcuts import redirect, render 
from .forms import *
from home.models import *
from django.contrib.auth import logout


def home(request):
    context = {'blogs': BlogModel.objects.all()}
    return render(request , 'home.html' , context)    


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request , 'register.html')    

def add_blog(request):

    context = {'form':BlogForm}
    try:
        if request.method == 'POST':
           
            form = BlogForm(request.POST)
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
            print('blog created ' , blog_obj)
            return redirect('/add-blog/')

    except Exception as e:
        print('<==========EXCEPTION=============>')
        print(e)
        print('<==========End EXCEPTION=========>')


    return render(request , 'add_blog.html' , context)

def blog_detail(request , slug):
    try:
        context = {'blog_obj': BlogModel.objects.filter(slug = slug).first()}
    except Exception as e:
        print('<==========EXCEPTION=============>')
        print(e)
        print('<==========End EXCEPTION=========>')
    
    return render(request , 'blog_details.html' , context)


def see_blog(request):
    context =  {}
    try:
        context['blog_objs'] = BlogModel.objects.filter(user = request.user)

    except Exception as e:
        print(e)
    
    return render(request , 'see_blog.html' , context)

def blog_delete(request , id):
    try:
        blog_obj = BlogModel.objects.get(id = id)
        
        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)    

    return redirect('/see-blog/')

def blog_update(request):
   return render(request , 'update_blog.html')


def logout_view(request):
    logout(request)
    return redirect('/')

def verify(request):
    pass