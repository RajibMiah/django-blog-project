from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(BlogModel)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = [ 'title']
admin.site.register(Profile)
admin.site.register(BlogModel)