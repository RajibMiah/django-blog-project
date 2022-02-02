from atexit import register
from django.urls import path 
from .views import *
urlpatterns = [
    path('login/' , loginView.as_view(), name="login_api"),
    path('register/' , RegisterView.as_view(), name = 'register_api')
]
