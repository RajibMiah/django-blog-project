from django.utils.text import slugify
import string
import random

'''
generated unique random slug
'''

  

def generate_random_string(N):
    res = ''.join(random.choice(string.ascii_uppercase + string.digits , k = N))
    return res

def generate_slug(text):
    new_slug = slugify(text)
    from home.models import BlogModel
    
    if BlogModel.objects.filter(slug = new_slug).first():
        return generate_slug(text + generate_random_string(5))
    return new_slug