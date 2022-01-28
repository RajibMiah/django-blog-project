from django.urls import path 
from .views import *
urlpatterns = [
    path('login/' , loginView.as_view(), name="login_view")
]
