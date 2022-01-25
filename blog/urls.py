from django.contrib import admin
from django.urls import path , include 

urlpatterns = [
    # path('', include('home.urls')),
    path('admin/', admin.site.urls),
    # path('froala_editor/',include('froala_editor.urls'))
]
