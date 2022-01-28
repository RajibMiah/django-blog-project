from atexit import register
from django.urls import path 
from .views import *
urlpatterns = [
    path('login/' , loginView.as_view(), name="login_view"),
    path('register/' , RegisterView.as_view(), name = 'register')
]
