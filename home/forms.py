from django import forms
from .models import *
from froala_editor.widgets import FroalaEditor

class BlogForm(forms.ModelForm):
  # content = forms.CharField(widget=FroalaEditor)
  class Meta:
        model = BlogModel
        fields = ['content']
  