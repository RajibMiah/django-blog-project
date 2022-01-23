from django.db import models
from froala_editor.fields import FroalaField


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    content = FroalaField()
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to = 'blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self) -> str:
    #     return self.title
