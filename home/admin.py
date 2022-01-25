from django.contrib import admin
from .models import BlogModel

# Register your models here.

# @admin.register(BlogModel)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = [ 'title']

admin.site.register(BlogModel)