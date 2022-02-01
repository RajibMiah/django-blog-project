from pyexpat import model
from django.db import models 
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helper import *

class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=255)



class BlogModel(models.Model):
    user = models.ForeignKey(User , blank=True , null=True , on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = FroalaField()
    slug = models.SlugField(max_length=255 , null= True , blank = True)
    image = models.ImageField(upload_to = 'blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self , *args , **kwargs):
        self.slug = generate_slug(self.title)
        super().save(*args , **kwargs)
