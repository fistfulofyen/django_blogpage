from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # auto_now_add=True automatically sets the field to now when the object is first created.
    # date_posted = models.DateTimeField(auto_now_add=True) # this cant be changed after creation
    date_posted = models.DateTimeField(default=timezone.now) # this can be changed after creation
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title