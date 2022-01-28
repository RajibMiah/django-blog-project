from django.urls import path, include

# app_name = 'home-api'

urlpatterns = [
    path('', include('home.api.base.urls')),
    # path('v1/', include('home.api.v1.url'))
]