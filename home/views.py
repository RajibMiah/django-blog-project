from django.shortcuts import render , HttpResponse

# Create your views here.
def tempalte(request):
    return HttpResponse("hello")


def home(request):
    return render(request , 'home.html')    


def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request , 'register.html')    

def add_blog(request):
    pass

def blog_detail(request):
    pass

def see_blog(request):
    pass

def blog_delete(request):
    pass

def blog_update(request):
    pass


def logout_view(request):
    pass

def verify(request):
    pass